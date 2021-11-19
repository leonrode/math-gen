from Node import Node
from Equation import Equation

from utils import generate_expression_tree, infix_to_postfix


equation = Equation(Node("="))

left_postfix = infix_to_postfix("x")
right_postfix = infix_to_postfix("5")

equation.setup_equation(Node.generate_expression_tree(left_postfix), Node.generate_expression_tree(right_postfix))


equation.exponent_expression(Node("2"))
print(equation)
equation.solve(equation.root.left)
print(equation)