class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 5 and n == 3:
            print("FizzBuzz")
        if n == 3:
            print("Fizz")
        if n == 5:
            print("Buzz")
        

n = 3
obj = Solution()
obj.fizzBuzz(n)