class Solution:
    def isValid(self, s: str) -> bool:
       list=[]
       list[:0]=s
       stack=[]
       if(len(s)==0):
           return True
       elif (s[0]==')' or s[0]==']' or s[0]=='}'):
           return False
       for elem in list: 
           if (elem=='(' or elem=='{' or elem=='['):
               stack.append(elem)
           elif(elem==')' or elem==']' or elem=='}'):
                  if(len(stack)==0 and ( elem==')' )):
                      return False;
                  elif(len(stack)==0 and ( elem=='}' )):
                      return False;
                  elif(len(stack)==0 and ( elem==']' )):
                      return False;
                  else:
                    value=stack.pop()
                    if (elem==')' and value!='('):
                        return False
                    elif(elem=='}' and value!='{'):
                        return False
                    elif(elem==']' and value!='['):
                        return False
                    
       print(stack) 
       if(len(stack)==0 ):
          return True
       else: 
           return False