class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        if len(timeSeries)==0:
            return 0
        seconds = 0
        lastattack = -1
        for i in timeSeries:
            if lastattack == -1:
                lastattack = i
            elif i-lastattack<=duration:
                x = i-lastattack
                lastattack = i
                seconds += x
            else:
                seconds+=duration
                lastattack = i
        seconds+=duration
        return seconds