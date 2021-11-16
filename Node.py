from utils import return_correct_number_type
from Stack import Stack


class Node:
    operators = ["+", "-", "*", "/", "^"]

    def __init__(self, value: str) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None

    @staticmethod
    def generate_expression_tree(postfix: str) -> "Node":
        operators = ["+", "-", "*", "/", "^"]
        stack = Stack()
        symbols = postfix.split(" ")

        for symbol in symbols:
            node = Node(symbol)

            if symbol not in operators:
                stack.push(node)
            else:

                right_operand: Node = stack.pop()
                left_operand: Node | None = None

                # we find an operator and the stack is empty,
                # meaning this operator is a unary operator.
                # the only unary operator defined so far is -
                if stack.size() != 0:
                    left_operand = stack.pop()

                node.left = left_operand
                node.right = right_operand
                stack.push(node)
        # at this point the only value is the root node

        return stack.pop()

    @staticmethod
    def expressions_equal(l_expression: "Node", r_expression: "Node") -> bool:

        if not l_expression and not r_expression:
            return True
        if not l_expression or not r_expression:
            return False

        if not Node.are_nodes_equal(l_expression, r_expression):
            return False

        if Node.expressions_equal(l_expression.left, r_expression.left) and Node.expressions_equal(l_expression.right, r_expression.right):
            return True

    @staticmethod
    def are_nodes_equal(l_node: "Node", r_node: "Node") -> bool:
        return l_node.value == r_node.value

    def is_unary_minus(self, node) -> bool:
        if node.value == "-" and node.right == None:
            return True
        return False

    def is_operator(self) -> bool:
        operators = ["+", "-", "*", "/", "^"]

        return self.value in operators

    def is_division(self):
        return self.value == "/"

    def is_addition(self):
        return self.value == "+"

    def is_subtraction(self):
        return self.value == "-"

    def is_multiplication(self):
        return self.value == "*"

    def is_exponent(self):
        return self.value == "^"

    def __str__(self):
        #print(self.left, self.right, self.value)
        res = ""
        parenthesize_expression = False

        if self.is_operator():
            parenthesize_expression = True
            res += "("

        if self.is_unary_minus(self):
            res += "("

            res += "-" + str(self.left)

            res += ")"
            return res

        if self.left:
            res += str(self.left)

        res += str(self.value)

        if self.right:
            res += str(self.right)

        if parenthesize_expression:
            res += ")"

        return res

    def is_value_direct_child(self, value) -> bool:
        return self.left.value == value or self.right.value == value

    def is_variable(self) -> bool:
        # a variable is a non-operator, alphabetic character
        return not self.is_operator() and not self.value.isnumeric()

    def is_number(self) -> bool:
        return self.value.isnumeric()

    def simplify(self) -> bool:
        simplified = self.apply_simplification_rule()
       # print(simplified)
        return simplified

    @staticmethod
    def copy_tree(node: "Node") -> "Node":
        if not node:
            return None

        new_node = Node(node.value)
        new_node.left = Node.copy_tree(node.left)
        new_node.right = Node.copy_tree(node.right)
        return new_node

    def operate(self) -> int | float:
        if not self.is_operator() or (not self.left.is_number() and not self.right.is_number()):
            print("no")
            return
        l_val = return_correct_number_type(self.left.value)
        r_val = return_correct_number_type(self.right.value)
        if self.value == "+":
            # print
            return l_val + r_val
        elif self.value == "-":
            return l_val - r_val
        elif self.value == "*":
            return l_val * r_val
        elif self.value == "/":
            return int(l_val / r_val) if (l_val / r_val == int(l_val / r_val)) else l_val / r_val
        elif self.value == "^":
            return l_val ** r_val

    def apply_simplification_rule(self) -> bool:

        # perform operation when both children are numbers
        if self.left and self.right:
            if self.left.is_number() and self.right.is_number() and self.is_operator():
                self.value = self.operate()
                self.left = None
                self.right = None
                return True
            # follow all algebraic rules when it comes to simplifying an expresesion
            # x * x = x^2
            if self.is_multiplication():

                if Node.expressions_equal(self.left, self.right):
                    self.value = Node("^")
                    # left expression squared
                    self.right = Node("2")
                    return True

                # x^y * x^z = x^(y + z)
                if self.left.is_exponent() and self.right.is_exponent():
                    if Node.are_nodes_equal(self.left.left, self.right.left):  # if x == x

                        tree = Node("^")
                        tree.left = Node.copy_tree(self.left.left)
                        tree.right = Node("+")
                        tree.right.left = Node.copy_tree(self.left.right)
                        tree.right.right = Node.copy_tree(self.right.right)

                        self.left = Node.copy_tree(tree.left)
                        self.right = Node.copy_tree(tree.right)
                        self.value = tree.value
                        return True
        return False
