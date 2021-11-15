from Node import Node
from Equation import Equation

from utils import generate_expression_tree, infix_to_postfix


equation = Equation(Node("="))

left_postfix = infix_to_postfix("x")
right_postfix = infix_to_postfix("5")

equation.setup_equation(generate_expression_tree(left_postfix), generate_expression_tree(right_postfix))
equation.do_operation_with_expression(Node("2"), "^")
print(equation)
equation.simplify()
print(equation)
equation.do_operation_with_expression(Node("9"), "-")
equation.simplify()
print(equation)
equation.do_operation_with_expression(Node("4"), "/")
equation.simplify()
print(equation)