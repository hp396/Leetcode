class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        list = s.split(" ")
        i = 0
        while i < int(len(list)):
            if i == int(len(list))-1:
                output +=list[i][::-1]
            else:
                output +=list[i][::-1]+ " "            
            i+=1
        return output
    
