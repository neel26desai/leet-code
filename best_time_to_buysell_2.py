class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0 
        for i in range(0,len(prices)-1):
            #selling day is i+1 and buying dat is i
            diff = prices[i+1] -prices[i]
            #if diff is positive add it to profit
            if diff>0:
                profit=profit+diff
        
        return profit


    
if __name__=="__main__":
    s= Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))
    prices = [1,2,3,4,5]
    print(s.maxProfit(prices))
    prices = [7,6,4,3,1]
    print(s.maxProfit(prices))
