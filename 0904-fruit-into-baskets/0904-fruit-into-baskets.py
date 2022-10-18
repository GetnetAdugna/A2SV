class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int) 
        left = 0
        answer = 0
        
        for right, f in enumerate(fruits):
            counter[f] += 1
            
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1
            answer = max(answer, right-left + 1)
        return answer
        