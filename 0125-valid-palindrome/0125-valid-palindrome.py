class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        s= re. sub(r'[\W_]', '', s) 
        print(s)
        
        if(len(s)%2==0):
            for i in range(len(s)//2):
                print(s[i])
                print(s[-1-i])
                
                if (s[i]!=s[-1-i]):
                    return False
            
        else:
            for i in range((len(s)-1)//2):
                 if (s[i]!=s[-1-i]):
                    return False
        return True
                
                
            
            
        