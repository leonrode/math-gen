from Node import Node
from Stack import Stack


class Equation:

    operators = ["+", "-", "*", "/", "^"]
    parens = ["(", ")"]

    def __init__(self, root) -> None:
        self.root = root

    def __str__(self):
        return str(self.root.left) + self.root.value + str(self.root.right)

    def set_left_side(self, tree) -> None:
        self.root.left = tree

    def set_right_side(self, tree) -> None:
        self.root.right = tree

    def setup_equation(self, left, right) -> None:
        self.root = Node("=")
        self.root.left = left
        self.root.right = right

    def add_expression_to_both_sides(self, expression) -> None:
        left_parent = Node("+")
        left_parent.left = expression
        left_parent.right = self.root.left

        right_parent = Node("+")
        right_parent.left = expression
        right_parent.right = self.root.right

        self.root.left = left_parent
        self.root.right = right_parent

    def get_all_nodes(self) -> list[Node]:
        nodes = []

        def traverse(node):
            if node:
                traverse(node.left)
                nodes.append(node)
                traverse(node.right)

        traverse(self.root)
        return nodes

    def operate(self, operation, l_operand, r_operand) -> int | float:
        if operation == "+":
            return l_operand + r_operand
        elif operation == "-":
            return l_operand - r_operand
        elif operation == "*":
            return l_operand * r_operand
        elif operation == "/":
            return l_operand / r_operand
        elif operation == "^":
            return l_operand ** r_operand

    def simplify(self) -> None:
        nodes = self.get_all_nodes()

        for node in nodes:
            if node.is_operator():
                if node.left.value.isnumeric() and node.right.value.isnumeric():
                    node.value = self.operate(
                        node.value, int(node.left.value), int(node.right.value))
                    node.left = None
                    node.right = None
