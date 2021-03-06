class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [None] * len(s)
        for i in s:
            newindex = indices.pop(0)
            output[newindex] = i
        return ''.join(output)