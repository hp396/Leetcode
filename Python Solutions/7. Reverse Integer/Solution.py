class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
        else:
            negative = False
        x = str(abs(x))
        x = int(x[::-1])
        if negative:
            if (abs(x) > (2**31)):
                return 0
            return -1 * int(x)
        else:
            if (abs(x) > (2**31)-1):
                return 0
            return x