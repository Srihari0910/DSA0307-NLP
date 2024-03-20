class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        self.input_string = input_string
        self.pos = 0
        self.current_token = None
        self.next_token()
        if self.start_production():
            if self.current_token is None:
                return True
        return False

    def next_token(self):
        if self.pos < len(self.input_string):
            self.current_token = self.input_string[self.pos]
            self.pos += 1
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.next_token()
            return True
        else:
            return False

    def start_production(self):
        return self.production_A()

    def production_A(self):
        if self.current_token is None:
            return False
        if self.current_token == 'a':
            return self.match('a') and self.production_A() and self.match('b')
        elif self.current_token == 'c':
            return self.match('c') and self.production_B()
        else:
            return False

    def production_B(self):
        if self.current_token is None:
            return False
        if self.current_token == 'b':
            return self.match('b') and self.production_B()
        elif self.current_token == 'd':
            return self.match('d')
        else:
            return False


# Example usage:
if __name__ == "__main__":
    grammar = {
        'A': [['a', 'A', 'b'], ['c', 'B']],
        'B': [['b', 'B'], ['d']]
    }
    parser = Parser(grammar)
    input_string = 'acbd'
    if parser.parse(input_string):
        print("Parsing successful!")
    else:
        print("Parsing failed!")
