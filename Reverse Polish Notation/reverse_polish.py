
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another
#     expression.
# Some examples:
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


def evalRPN(array):
    stack = []
    for element in array:
        if element in {"+", "-", "*", "/"}:
            if element == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif element == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif element == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif element == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 / num2)
        else: 
            stack.append(int(element))
    
    return stack.pop()

array = ["2", "1", "+", "3", "*"]
print(array)
print(evalRPN(array))

array = ["4", "13", "5", "/", "+"]
print(array)
print(evalRPN(array))

