from Node import Node
from Equation import Equation

from utils import generate_expression_tree, infix_to_postfix


equation = Equation(Node("="))

left_postfix = infix_to_postfix("(-(x+5))/7")
right_postfix = infix_to_postfix("10")

left_expression = generate_expression_tree(left_postfix)
right_expression = generate_expression_tree(right_postfix)

equation.setup_equation(left_expression, right_expression)
print(equation)
