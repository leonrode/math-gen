from Stack import Stack
class Node:

    def __init__(self, value: str) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None


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

    def is_unary_minus(self, node) -> bool:
        if node.value == "-" and node.right == None:
            return True
        return False

    def is_numerical(self) -> bool:
        return self.value.is_digit()

    def is_operator(self) -> bool:
        operators = ["+", "-", "*", "/", "^"]

        return self.value in operators
    
    def is_division_operator(self):
        return self.value == "/"
    
    def is_addition_operator(self):
        return self.value == "+"
    def is_subtraction_operator(self):
        return self.value == "-"
    def is_multiplication_operator(self):
        return self.value == "*"
    def is_exponent_operator(self):
        return self.value == "^"
    
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


        # if the expression would be 2*x: we just want 2x
        if self.value != "*":
            res += str(self.value)

        if self.right:
            res += str(self.right)

        if parenthesize_expression:
            res += ")"

        return res
