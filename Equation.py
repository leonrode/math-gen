from Node import Node
from Stack import Stack


class Equation:

    operators = ["+", "-", "*", "/", "^"]
    parens = ["(", ")"]

    def __init__(self, root) -> None:
        self.root = root

    def __str__(self):
        string = str(self.root.left) + self.root.value + str(self.root.right)

        stripped = ""
        # remove unnecessary parens
        # TODO
        return str(self.root.left) + self.root.value + str(self.root.right)

    def set_left_side(self, tree: Node) -> None:
        self.root.left = tree

    def set_right_side(self, tree: Node) -> None:
        self.root.right = tree

    def setup_equation(self, left: Node, right: Node) -> None:
        self.root = Node("=")
        self.root.left = left
        self.root.right = right

    def add_expression(self, expression: Node, toRight: bool = False) -> None:
        self.do_operation_with_expression(expression, "+", toRight)
        # left_parent = Node("+")
        # left_parent.left = expression
        # left_parent.right = self.root.left

        # right_parent = Node("+")
        # right_parent.left = expression
        # right_parent.right = self.root.right

        # self.root.left = left_parent
        # self.root.right = right_parent
    
    def multiply_expression(self, expression: Node, toRight: bool = False) -> None:
        self.do_operation_with_expression(expression, "*", toRight)
        # left_parent = Node("*")
        # left_parent.left = expression
        # left_parent.right = self.root.left

        # right_parent = Node("*")
        # right_parent.left = expression
        # right_parent.right = self.root.right

        # self.root.left = left_parent
        # self.root.right = right_parent
    def divide_expression(self, expression: Node, toRight: bool = False) -> None:
        self.do_operation_with_expression(expression, "/", toRight)
        # left_parent = Node("/")
        # left_parent.left = expression
        # left_parent.right = self.root.left

        # right_parent = Node("/")
        # right_parent.left = expression
        # right_parent.right = self.root.right

        # self.root.left = left_parent
        # self.root.right = right_parent

    def exponent_expression(self, expression: Node) -> None:
        self.do_operation_with_expression(expression, "^", True)
    
    def subtract_expression(self, expression: Node, toRight: bool = False) -> None:
        self.do_operation_with_expression(expression, "-", toRight)
        # left_parent = Node("-")
        # left_parent.left = expression
        # left_parent.right = self.root.left

        # right_parent = Node("-")
        # right_parent.left = expression
        # right_parent.right = self.root.right

        # self.root.left = left_parent
        # self.root.right = right_parent
    
    def do_operation_with_expression(self, expression: Node, operation: str, toRight: bool = True) -> None:
        left_parent = Node(operation)
        # print(self.root.left, expression, operation)
        if toRight:
            left_parent.left = self.root.left
            left_parent.right = expression
            # print(left_parent)
        else:
            
            left_parent.right = self.root.left
            left_parent.left = expression
        right_parent = Node(operation)
        if toRight:
            right_parent.left = self.root.right
            right_parent.right = expression
        else:
            right_parent.right = self.root.right
            right_parent.left = expression
        # print(left_parent, right_parent)
        self.root.left = left_parent
        self.root.right = right_parent
    def get_all_nodes(self) -> list[Node]:
        nodes = []

        def traverse(node):
            if node:
                print(node)
                traverse(node.left)
                nodes.append(node)
                traverse(node.right)

        traverse(self.root)
        return nodes

    def operate(self, operation: str, l_operand: int | float, r_operand: int | float) -> int | float:
        if operation == "+":
            return l_operand + r_operand
        elif operation == "-":
            return l_operand - r_operand
        elif operation == "*":
            return l_operand * r_operand
        elif operation == "/":
            print(l_operand, r_operand, type(l_operand), type(r_operand))
            return int(l_operand / r_operand) if (l_operand / r_operand == int(l_operand / r_operand)) else l_operand / r_operand
        elif operation == "^":
            return l_operand ** r_operand


    def simplify(self) -> None:
        nodes = self.get_all_nodes()

        for node in nodes:
            if node.is_operator():
                print(node.left.value, node.right.value)
                print(type(node.left.value), type(node.right.value))
                if node.left.value.isnumeric() and node.right.value.isnumeric():
                    node.value = str(self.operate(
                        node.value, int(node.left.value), int(node.right.value)))
                    node.left = None
                    node.right = None
                
                if node.is_division_operator():
                    if Node.expressions_equal(node.left, node.right):
                        # something like (x+5)/(x+5)
                        node.value = "1"
                        node.left = None
                        node.right = None

    """TODO: WORK ON IT"""
    def solve(self, node: Node) -> None:
        if not node.value.isdigit() and not node.value in self.operators:
                return 
        if node:
            print(node)
            if node.value not in self.operators or ( not node.left and not node.right):

                return int(node.value) if node.value == int(node.value) else float(node.value)

            
            left = self.solve(node.left)
            right = self.solve(node.right)
            print(left, right)
            if left and right:
                if node.value == "+":
                    return left + right
                elif node.value == "-":
                    return left - right
                elif node.value == "*":
                    return left * right
                elif node.value == "/":
                    return left / right
                elif node.value == "^":
                    return left ** right
            