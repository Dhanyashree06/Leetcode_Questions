# 1288. Remove Covered Intervals

class Solution:
    def removeCoveredIntervals(self, intervals):
        # Sort by left ascending, and right descending
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        maxRight = 0

        for left, right in intervals:
            if right > maxRight:
                count += 1
                maxRight = right

        return count
    
