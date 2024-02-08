# Since we traverse the string of n characters once, the time complexity for this algorithm is O(n).
def evaluate_postfix(expression):
    operands = []
    for char in expression:
        if char.isdigit():
            operands.append(char)
        else:
            right = operands.pop()
            left = operands.pop()
            
            operands.append(str(eval(left + char + right)))
    return int(float(operands.pop()))



if __name__ == "__main__":
    expr = "82/3+"
    print(evaluate_postfix(expr))
