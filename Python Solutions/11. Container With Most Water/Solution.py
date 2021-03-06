class Solution:
    def maxArea(self, height: List[int]) -> int:
        index = 0
        output = 0
        revindex = len(height)-1
        while index < len(height)-1 and revindex>=0:
            if height[index] < height[revindex]:
                temp_container = height[index] * (abs(revindex-index))
                index+=1
            elif height[index] > height[revindex]:
                temp_container = height[revindex] * (abs(revindex-index))
                revindex-=1
            else:
                temp_container = height[index] * (abs(revindex-index))
                index+=1
            if temp_container > output:     
                output = temp_container
            if revindex == index:
                break
        return output