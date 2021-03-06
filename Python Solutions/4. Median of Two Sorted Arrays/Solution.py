class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = self.mergedarray(nums1,nums2)
        print(num)
        if len(num) % 2 != 0:
            return num[(int(len(num)/2 - 0.5))]
        else:
            return (num[int(len(num)/2)] + num[int(len(num)/2)-1])/2
        
    def mergedarray(self,nums1,nums2):
        if len(nums1) == 0:
            return nums2
        elif len(nums2) == 0:
            return nums1
        else:
            return sorted(nums1 + nums2)
