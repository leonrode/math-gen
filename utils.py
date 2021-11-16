from Stack import Stack

operators = ["+", "-", "*", "/", "^"]
parens = ["(", ")"]


def precedence(operator: str) -> int:
    if operator == "^":
        return 3
    elif operator in ["/", "*"]:
        return 2
    elif operator in ["+", "-"]:
        return 1
    elif operator == "(":
        return 0


def infix_to_postfix(infix: str) -> str:

    stack: Stack = Stack()
    postfix: list[str] = []
    symbols = infix.split(" ")

    for symbol in symbols:
        # if operand
        if symbol not in operators and symbol not in parens:
            postfix.append(symbol)
        elif symbol == "(":
            stack.push(symbol)
        elif symbol == ")":
            # pop until ( is found
            while stack.peek() != "(":
                postfix.append(stack.pop())
            stack.pop()  # remove (
        elif symbol in operators:
            while stack.size() > 0 and precedence(stack.peek()) >= precedence(symbol):
                postfix.append(stack.pop())
            stack.push(symbol)
    while stack.size() > 0:
        postfix.append(stack.pop())

    return " ".join(postfix)


# In the case of division and exponentiation...
# division: (node.left) / (node.right)
# exponentiation: (node.left) ** (node.right)


# Return an integer if the string represents an integer, otherwise a float
def return_correct_number_type(value: str) -> int | float:
    value = float(value)
    if value.is_integer():
        return int(value)
    return value
