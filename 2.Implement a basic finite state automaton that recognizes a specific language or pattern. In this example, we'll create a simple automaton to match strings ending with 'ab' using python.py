class FiniteStateMachine:
    def __init__(self):
        self.transitions = {
            'q0': {'a': 'q0', 'b': 'q1'},
            'q1': {'a': 'q0', 'b': 'q2'},
            'q2': {'a': 'q2', 'b': 'q2'}
        }
        self.initial_state = 'q0'
        self.accepting_states = {'q2'}

    def process_input(self, input_string):
        current_state = self.initial_state
        for char in input_string:
            if char not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][char]
        return current_state in self.accepting_states

def main():
    fsm = FiniteStateMachine()

    
    test_strings = ["ab", "bab", "aaab", "abab", "b", "a", "bbb"]

    for test_string in test_strings:
        if fsm.process_input(test_string):
            print(f"'{test_string}' is accepted.")
        else:
            print(f"'{test_string}' is not accepted.")

if __name__ == "__main__":
    main()
