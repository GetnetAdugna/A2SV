class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        listof = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                listof.append("FizzBuzz")
            elif i%3==0:
                listof.append("Fizz")
                
            elif i%5==0:
                listof.append("Buzz")
                
            else:
                listof.append(str(i))
                
        return listof