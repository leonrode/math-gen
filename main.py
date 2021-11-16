from Node import Node
from Equation import Equation

from utils import infix_to_postfix


postfix = infix_to_postfix("( x ^ 2 ) * ( x ^ 5 )")
tree = Node.generate_expression_tree(postfix)

# print(tree)
equation = Equation(Node("="))
equation.set_left_side(tree)
equation.simplify()
print(equation)
