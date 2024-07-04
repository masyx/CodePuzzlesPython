class Solution:
    # O(n) time | O(n) space
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            temp = ''
            if i % 3 == 0 and i % 5 == 0:
                temp = "FizzBuzz"
            elif i % 3 == 0:
                temp = "Fizz"
            elif i % 5 == 0:
                temp = "Buzz"
            else:
                temp = f"{i}"
            answer.append(temp)
        return answer
    
    
    def fizzBuzz_2(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


    def fizzBuzz_3(self, n):
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) 
                for i in range(1, n + 1)]


    def fizzBuzz_4(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            temp = ''
            if i % 3 != 0 and i % 5 != 0:
                temp = str(i)
            else:
                temp = "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)
            answer.append(temp)
        return answer
    
        
    def fizz_buzz_5(n):
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

    def fizz_buzz_6(n):
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

    
    
def main():
    sol = Solution()
    print(sol.fizzBuzz_4(5))
    
    
if __name__ == "__main__":
    main()