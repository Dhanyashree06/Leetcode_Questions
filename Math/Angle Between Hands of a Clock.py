# 1344. Angle Between Hands of a Clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Minute hand angle
        minute_angle = minutes * 6

        # Hour hand angle
        hour_angle = (hour % 12) * 30 + minutes * 0.5

        angle = abs(hour_angle - minute_angle)

        return min(angle, 360 - angle)  
