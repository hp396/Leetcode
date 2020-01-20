class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        counter = 0
        i = 0
        while counter<len(A):
            if A[i]%2!=0:
                A.append(A.pop(i))
                i-=1
            i+=1
            counter += 1           
        return A
