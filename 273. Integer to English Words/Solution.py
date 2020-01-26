class Solution:
    def __init__(self):
        self.hmap = {
            0:"",
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen",
            20:"Twenty",
            30:"Thirty",
            40:"Forty",
            50:"Fifty",
            60:"Sixty",
            70:"Seventy",
            80:"Eighty",
            90:"Ninety",
        }
    def numberToWords(self, num: int) -> str:        
        if num == 0:
            return "Zero"

        output = []   
        if num >=1000000000:
            output += self.helper(num//1000000000)
            output.append("Billion")
            num = num%1000000000
        if num >=1000000:
            output += self.helper(num//1000000)
            output.append("Million")
            num = num%1000000
        if num >=1000:
            output += self.helper(num//1000)
            output.append("Thousand")
            num = num%1000
        output += self.helper(num)

        while '' in output:
            output.remove('')
        return " ".join(output)
        
        
    def helper(self,i):
        if i <20: 
            return [self.hmap.get(i)]
        if i <100:
            return [self.hmap.get((i//10)*10) ,self.hmap.get(i%10)]
        if i < 1000:
            returnl = []
            returnl.append(self.hmap.get((i//100)))
            returnl.append("Hundred")
            if i%100<20:
                returnl.append(self.hmap.get(i%100))
            else:
                returnl.append(self.hmap.get(((i%100)//10)*10))
                returnl.append(self.hmap.get(i%10))
            return returnl
            
        
