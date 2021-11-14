from Node import Node
from Stack import Stack


class Equation:
    #paren_operators = ["+", "-", "*", "/", "^"]
    operators = ["+", "-", "*", "/", "^"]
    parens = ["(", ")"]

    def __init__(self, root):
        self.root = root

    def init_left(self, tree):
        self.root.left = tree

    def init_right(self, tree):
        self.root.right = tree

    def setup_equation(self, left, right):
        self.root = Node("=")
        self.root.left = left
        self.root.right = right

    def is_unary_minus(self, node):
        if node.value == "-" and node.right == None:
            return True
        return False

    def print_tree(self, node):
        res = ""

        if node:

            if node.value in self.operators:
                res = res + "("
            if self.is_unary_minus(node):

                res = res + "("

                res = res + "-" + node.left.value

                if node.value in self.operators:
                    res = res + ")"
                return res

            res = res + self.print_tree(node.left)

            res += node.value

            res = res + self.print_tree(node.right)
            if node.value in self.operators:
                res = res + ")"

        return res

    def read_postfix(self, postfix) -> Node:
        # goal
        # read something like x+5 or (x * 5) / 5
        stack = Stack()
        symbols = postfix.split(" ")

        for symbol in symbols:
            node = Node(symbol)
            if symbol not in self.operators:
                stack.push(node)
            else:

                right_operand = stack.pop()
                left_operand = stack.pop()
                node.left = left_operand
                node.right = right_operand
                stack.push(node)
        # at this point the only value is the root node

        return stack.pop()
