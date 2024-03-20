from pyparsing import Word, alphas, alphanums, Forward, oneOf, Optional, ZeroOrMore, Group, Suppress

# Define basic elements
variable = Word(alphas, alphanums + "_")
quantifier = oneOf("forall exists")
operator = oneOf("and or implies iff not")
open_parenthesis = Suppress("(")
close_parenthesis = Suppress(")")

# Define the FOPC grammar
expression = Forward()

atom = Group(variable + Optional("(" + Group(variable + ZeroOrMore("," + variable)) + ")"))
term = atom | variable

quantified_expr = Group(quantifier + variable + expression)
unary_expr = Group(operator + expression)
binary_expr = Group(open_parenthesis + expression + operator + expression + close_parenthesis)

expression << (quantified_expr | unary_expr | binary_expr | term)

# Parse FOPC expression
def parse_fopc(input_str):
    return expression.parseString(input_str, parseAll=True)

# Test the parser
if __name__ == "__main__":
    input_expression = "forall x (P(x) and Q(x, y))"
    result = parse_fopc(input_expression)
    print(result)
