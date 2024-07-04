def fizz_buzz(n):
    result = [i for i in range(1, n + 1)]
    for i in range(1, n + 1):
        current = ["", ""]
        if i % 3 == 0:
            current[0] = "Fizz"
        if i % 5 == 0:
            current[1] = "Buzz"
        if current[0] or current[1]:
            result[i - 1] = "".join(current)
    return result

def fizz_buzz_2(n):
    result = [str(i + 1) for i in range(n)]
    for i in range(1, n + 1):
        curr = ""
        if i % 3 == 0:
            curr += "Fizz"
        if i % 5 == 0:
            curr += "Buzz"
        if curr:
            result[i - 1] = curr
    return result

            

if __name__ == "__main__":
    prices = [1]
    print(fizz_buzz_2(15))