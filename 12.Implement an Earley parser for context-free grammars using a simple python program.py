def predict(productions, state, chart):
    for production in productions:
        if state[2] < len(production[1]):
            chart.append((production[0], production[1], 0, state[1]))

def scan(word, state, chart):
    if state[2] < len(state[0]) and state[0][state[2]] == word:
        chart.append((state[0], state[1], state[2] + 1, state[3]))

def complete(state, chart):
    for st in chart:
        if state[2] < len(st[0]) and st[0][state[2]] == state[1][state[3]]:
            chart.append((st[0], st[1], st[2] + 1, st[3]))

def earley_parser(grammar, input_str):
    chart = [(('S', ['E']), 'E', 0, 0)]
    productions = grammar

    for i, word in enumerate(input_str.split()):
        for state in chart:
            if state[2] < len(state[0]) and state[0][state[2]] in grammar:
                predict(productions, state, chart)
            else:
                scan(word, state, chart)

        j = 0
        while j < len(chart):
            state = chart[j]
            if state[2] == len(state[0]):
                complete(state, chart)
            j += 1

    return chart

def main():
    grammar = [
        ('E', ['E', '+', 'T']),
        ('E', ['T']),
        ('T', ['T', '*', 'F']),
        ('T', ['F']),
        ('F', ['(', 'E', ')']),
        ('F', ['num'])
    ]

    input_str = "3 + 4 * (5 + 2)"
    chart = earley_parser(grammar, input_str)

    for i, state in enumerate(chart):
        if state[0] == ('S', ['E']) and state[2] == 6:
            print("Input string is valid.")
            break
        elif i == len(chart) - 1:
            print("Input string is not valid.")

if __name__ == "__main__":
    main()
