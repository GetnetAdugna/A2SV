class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split(" ")
        temp=0
        newstring=[]
        for i in range(len(words)):
            for j in range((i+1),len(words)):
                if(words[i][-1]>words[j][-1]):
                    temp=words[i]
                    words[i]=words[j]
                    words[j]=temp
       
        for i in range(len(words)):
           newstring.append( f"{words[i][:-1]}")
     
        s=" ".join([str(elem) for elem in newstring])
        return s
        