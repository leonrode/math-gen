class Node:

    def __init__(self, value) -> None:
        self.value: str = value
        self.left: Node = None
        self.right: Node = None

    def is_unary_minus(self, node) -> bool:
        if node.value == "-" and node.right == None:
            return True
        return False

    def is_numerical(self) -> bool:
        return self.value.is_digit()

    def is_operator(self) -> bool:
        operators = ["+", "-", "*", "/", "^"]

        return self.value in operators

    def __str__(self):
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
