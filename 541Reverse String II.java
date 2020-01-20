class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # output = []
        if int(len(s)) <k:
            return s[0:k][::-1]
        if int(len(s)) < 2*k and int(len(s)) >= k:
            return s[0:k][::-1] + s[k:]
        output = []
        stri = list(s)
        end = int(len(stri))
        for index in range(0,end,2*k):
            output += stri[index:index+k][::-1] 
            output += stri[index + k: index+2*k]
            
        return ''.join(output)
