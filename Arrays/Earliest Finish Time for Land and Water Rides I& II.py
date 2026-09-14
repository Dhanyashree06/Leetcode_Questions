# 3633. Earliest Finish Time for Land and Water Rides I

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        ans = float('inf')

        n = len(landStartTime)
        m = len(waterStartTime)

        for i in range(n):
            for j in range(m):

                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(land_finish, waterStartTime[j])
                ans = min(ans, water_start + waterDuration[j])

                # Water -> Land
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(water_finish, landStartTime[i])
                ans = min(ans, land_start + landDuration[i])

        return ans