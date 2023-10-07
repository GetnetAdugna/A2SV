class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit=0
        if(n==1):
            return 0
        buy,sell=0,1

        
        
        while(sell<n):
                while((prices[sell]-prices[buy])<0):
                    if(sell<n-1):
                        buy=sell
                        sell=buy+1
                    else:
                        break
              
         
                profit=prices[sell]-prices[buy]
              
                if(max_profit<profit):
                    max_profit=profit
                sell+=1
                    
        return max_profit
                
            