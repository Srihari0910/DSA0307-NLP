class PluralFiniteStateMachine:
    def __init__(self):
        self.transitions = {
            'q0': {'s': 'q1', 'x': 'q1', 'z': 'q1', 'ch': 'q1', 'sh': 'q1'},
            'q1': {'y': 'q2'},
        }
        self.initial_state = 'q0'
        self.accepting_states = {'q1', 'q2'}

    def process_input(self, noun):
        current_state = self.initial_state
        for i in range(len(noun) - 1, -1, -1):
            suffix = noun[i:]
            if suffix in self.transitions[current_state]:
                current_state = self.transitions[current_state][suffix]
            else:
                break
        return current_state in self.accepting_states

    def generate_plural(self, noun):
        if self.process_input(noun):
            return noun + 'es'
        else:
            return noun + 's'

def main():
    fsm = PluralFiniteStateMachine()

    # Test nouns
    test_nouns = ["cat", "dog", "church", "fox", "bush", "toy"]

    for test_noun in test_nouns:
        print(f"Plural of '{test_noun}': {fsm.generate_plural(test_noun)}")

if __name__ == "__main__":
    main()
