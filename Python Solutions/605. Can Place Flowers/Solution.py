class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        output = 0
        index = 0
        pickedli = []
        while index <= len(flowerbed)-1:
            if flowerbed[index] == 0 and index-1 not in pickedli:
                if index == len(flowerbed)-1:
                    
                    if flowerbed[index-1] == 0:
                        output+=1
                        pickedli.append(index)
                elif index == 0:
                    if flowerbed[index+1] == 0:
                        output+=1
                        pickedli.append(index)
                
                else:
                    if flowerbed[index+1] ==0 and flowerbed[index-1]==0:
                        output+=1
                        pickedli.append(index)
                        
            if output == n: return True
            index+=1
        if output >= n:
            return True
        else: return False