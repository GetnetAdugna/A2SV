class Solution:
   def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s :
            if i=="(" or i!=")" :
                stack.append(i)
            elif i==")" :
                temp=[]
                while stack[-1] != "(" :
                    
                    temp.append(stack.pop())
                stack.pop()
                for i in temp :
                    stack.append(i)
        output=""
        for i in stack :
            output+=i
        return output
        