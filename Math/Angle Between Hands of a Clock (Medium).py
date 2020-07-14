# 1344. Angle Between Hands of a Clock
# Tags - Math

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hrDeg = (hour * 30) if hour != 12 else 0 
        hrDeg += (minutes/2)
        minDeg = minutes * 6
        diff = abs(hrDeg - minDeg)
        return min(diff, 360 - diff)