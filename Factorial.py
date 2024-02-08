# really good article about recursion https://www.programiz.com/python-programming/recursion
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
        
def factorial_stack(n):
    stack = []
    while n > 0:
        stack.append(n)
        n -= 1
    
    result = 1
    while stack:
        result *= stack.pop()
    
    return result

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    print(factorial(16))
    
    
if __name__ == "__main__":
    main()