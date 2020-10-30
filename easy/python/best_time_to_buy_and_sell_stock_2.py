"""
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
    Input: [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
    Input: [2,4,1]
    Output: 2

Example 3:
    Input: [1,2,3,4,5]
    Output: 4
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buying_price_index = 0
        highest_selling_price_index = 0
        total_profit = 0
        
        for day in range(1, len(prices)):
            # Price is increasing
            if prices[day] > prices[lowest_buying_price_index]:
                if prices[day] > prices[highest_selling_price_index]:
                    highest_selling_price_index = day
                else:
                    total_profit += prices[highest_selling_price_index] - prices[lowest_buying_price_index]
                    lowest_buying_price_index = 0
                    highest_selling_price_index = 0
            
            # Price is decreasing or staying the same
            if prices[day] <= prices[lowest_buying_price_index]: 
                lowest_buying_price_index = day
                highest_selling_price_index = day
            
            # Price keep increasing until the end  
            if day == len(prices) - 1 and prices[day] > prices[lowest_buying_price_index]:
                total_profit += prices[highest_selling_price_index] - prices[lowest_buying_price_index]
        
        return total_profit
                