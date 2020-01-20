class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        counter = 0
        while m < int(len(nums1)):
            if nums1[m]==0:
                nums1[m] = nums2[counter]
            m+=1
            counter+=1
        nums1.sort()
