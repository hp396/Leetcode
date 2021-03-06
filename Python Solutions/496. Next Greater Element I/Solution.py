class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        compare2 = set(nums2)
        for i in nums1:
            added = False
            if i in compare2:
                index = nums2.index(i)
            else: index = 0
            for j in nums2[index:]:
                if i < j:
                    output.append(j)
                    added = True
                    break
            if added == False:
                output.append(-1)
                added = False
        return output