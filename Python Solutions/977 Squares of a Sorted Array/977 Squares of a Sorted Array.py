class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        index = 0
        for i in A:
            A[index] = i * i
            index += 1
        A.sort()
        return A        
