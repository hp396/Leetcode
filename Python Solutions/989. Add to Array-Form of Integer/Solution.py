class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num=""
        for i in A:
            num += str(i)
        # num = ''.join(A)
        output = int(num)+K
        return [int(x) for x in str(output)] 