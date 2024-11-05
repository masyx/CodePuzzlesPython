class Solution:
    def fizzBuzz_best(self, n):
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
    
    def fizzBuzz_secondToBest(self, n: int):
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
    
def main():
    sol = Solution()
    print("\n".join(sol.fizzBuzz_best(15)))
    
    
if __name__ == "__main__":
    main()