def is_happy_number(n):
    numbers_seen = set()
    def is_happy_number_helper(n):
        numbers_seen.add(n)
        
        result = 0
        while n > 0:
            number = n % 10
            result += number**2
            n //= 10
        
        if result == 1:
            return True
        elif result in numbers_seen:
            return False
        else:
            return is_happy_number_helper(result)
    return is_happy_number_helper(n)


if __name__ == "__main__":
    number = 2
    print(f"Is {number} a happy number? - {is_happy_number(number)}")