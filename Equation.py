from Node import Node
from Stack import Stack


class Equation:

    operators = ["+", "-", "*", "/", "^"]
    parens = ["(", ")"]

    def __init__(self, root) -> None:
        self.root = root

    def __str__(self):
        return str(self.root.left) + self.root.value + str(self.root.right)

    def set_left_side(self, tree: Node) -> None:
        self.root.left = tree

    def set_right_side(self, tree: Node) -> None:
        self.root.right = tree

    def setup_equation(self, left: Node, right: Node) -> None:
        self.root = Node("=")
        self.root.left = left
        self.root.right = right

    def add_expression(self, expression: Node) -> None:
        left_parent = Node("+")
        left_parent.left = expression
        left_parent.right = self.root.left

        right_parent = Node("+")
        right_parent.left = expression
        right_parent.right = self.root.right

        self.root.left = left_parent
        self.root.right = right_parent

    def multiply_expression(self, expression: Node) -> None:
        left_parent = Node("*")
        left_parent.left = expression
        left_parent.right = self.root.left

        right_parent = Node("*")
        right_parent.left = expression
        right_parent.right = self.root.right

        self.root.left = left_parent
        self.root.right = right_parent

    def divide_expression(self, expression: Node) -> None:
        left_parent = Node("/")
        left_parent.left = expression
        left_parent.right = self.root.left

        right_parent = Node("/")
        right_parent.left = expression
        right_parent.right = self.root.right

        self.root.left = left_parent
        self.root.right = right_parent

    def subtract_expression(self, expression: Node) -> None:
        left_parent = Node("-")
        left_parent.left = expression
        left_parent.right = self.root.left

        right_parent = Node("-")
        right_parent.left = expression
        right_parent.right = self.root.right

        self.root.left = left_parent
        self.root.right = right_parent

    def do_operation_with_expression(self, expression: Node, operation: str) -> None:
        left_parent = Node(operation)
        left_parent.left = self.root.left
        left_parent.right = expression

        right_parent = Node(operation)
        right_parent.left = self.root.right
        right_parent.right = expression

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

    def simplify(self) -> None:
        nodes = self.get_all_nodes()

        simplify_again = False
        for node in nodes:

            if node.apply_simplification_rule():
                simplify_again = True

        if simplify_again:
            self.simplify()
