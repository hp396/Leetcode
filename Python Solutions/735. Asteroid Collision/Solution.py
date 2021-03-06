class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        index = 0
        for i in asteroids:
            if len(output) == 0:
                index = 0
            if index == 0:
                output.append(i)
                index+=1
                continue
            elif output[-1]<0 and i >=0:
                output.append(i)
            elif output[-1]>=0 and i >=0:
                output.append(i)
            else:
                append = True
                while True:
                    if output[-1]<0:
                        break
                    elif abs(output[-1]) == abs(i):
                        del output[-1]
                        append = False
                        break
                    elif abs(output[-1]) < abs(i):
                        del output[-1]
                    else:
                        append = False
                        break
                    if len(output)==0:
                        break
                if append:
                    output.append(i)
        return output