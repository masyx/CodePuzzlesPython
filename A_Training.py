def is_happy_number(n):
    def sum_of_squares(number):
        total = 0
        while number > 0:
            digit = number % 10
            total += digit**2
            number //= 10
        return total
    
    numbers_seen = set()
    
    while n != 1 and n not in numbers_seen:
        numbers_seen.add(n)
        n = sum_of_squares(n)
        
    return n == 1


if __name__ == "__main__":
    number = 23
    print(f"Is {number} a happy number? - {is_happy_number(number)}")