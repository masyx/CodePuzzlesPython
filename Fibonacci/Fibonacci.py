def main():
    print(getNthFib(4))
    
def getNthFib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    
    return getNthFib(n - 2) + getNthFib(n - 1)
    
    

if __name__ == "__main__":
    main()