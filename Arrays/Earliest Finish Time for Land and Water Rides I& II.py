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

#3635. Earliest Finish Time for Land and Water Rides II

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def solve(start1, duration1, start2, duration2):
            finish1 = inf
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])
            finish2 = inf
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])
            return finish2

        land_water = solve(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        water_land = solve(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        return min(land_water, water_land)