from Node import Node
from Stack import Stack


class Equation:
    # paren_operators = ["+", "-", "*", "/", "^"]
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

    def __str__(self):
        return str(self.root.left) + self.root.value + str(self.root.right)
