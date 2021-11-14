from Stack import Stack
from Node import Node
operators = ["+", "-", "*", "/", "^"]
parens = ["(", ")"]


def precedence(operator):
    if operator == "^":
        return 3
    elif operator in ["/", "*"]:
        return 2
    elif operator in ["+", "-"]:
        return 1
    elif operator == "(":
        return 0


def infix_to_postfix(infix):

    stack = Stack()
    postfix = []
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


def generate_expression_tree(postfix):
    stack = Stack()
    symbols = postfix.split(" ")

    for symbol in symbols:
        node = Node(symbol)
        if symbol not in operators:
            stack.push(node)
        else:

            right_operand = stack.pop()
            left_operand = stack.pop()
            node.left = left_operand
            node.right = right_operand
            stack.push(node)
    # at this point the only value is the root node

    return stack.pop()
