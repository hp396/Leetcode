class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output = set()
        for i in nums:
            if i in output:
                output.remove(i)
            else:
                output.add(i)
        return list(output)