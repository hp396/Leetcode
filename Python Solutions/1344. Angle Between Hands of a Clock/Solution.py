class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourangle = ((hour*60)+minutes)*0.5
        minangle = minutes*6
        angle = abs(hourangle-minangle)
        if angle < 360-angle:
            return angle
        else: return 360-angle