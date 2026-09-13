# 2144. Minimum Cost of Buying Candies With Discount

class Solution:
    def minimumCost(self, cost):

        cost.sort(reverse=True)

        total = 0

        for i in range(len(cost)):

            if i % 3 != 2:   # skip every 3rd candy
                total += cost[i]

        return total