class Solution:
    def removeDuplicates(self, S: str) -> str:
        #456ms 5.07, 13.1mb 100
        # output = []
        # output.append(S[0])
        # for i in S[1:]:
        #     if len(output)>0 and output[-1] == i:
        #         output = output[:-1]
        #     else:
        #         output.append(i)
        
        
        #Discussion: 80ms 55.8, 12.8mb 100
        # stack = ""
        # for i in range(len(S)):
        #     if not stack or S[i]!=stack[-1]:
        #         stack+=S[i]
        #     else:
        #         stack=stack[:-1]
        # return stack
        
        
        #92ms 40.62, 12.7mb 100
        
        output = S[0]
        for i in S[1:]:
            

            if len(output) == 0 or output[-1] != i:
                output+=i
            else:
                output = output[:-1]
        return output