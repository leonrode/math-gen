class Node:
    operators = ["+", "-", "*", "/", "^"]

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_unary_minus(self, node):
        if node.value == "-" and node.right == None:
            return True
        return False

    def __str__(self):
        res = ""
        parenthesize_expression = False

        if self.value in self.operators:
            parenthesize_expression = True
            res += "("

        if self.is_unary_minus(self):
            res += "("

            res += "-" + str(self.left)

            res += ")"
            return res

        if self.left:
            res += str(self.left)

        res += self.value

        if self.right:
            res += str(self.right)

        if parenthesize_expression:
            res += ")"

        return res
