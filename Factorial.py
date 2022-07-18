# really good article about recursion https://www.programiz.com/python-programming/recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        


def main():
    print(factorial(1))
    
    
if __name__ == "__main__":
    main()