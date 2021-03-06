class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.translate(str.maketrans('', '', string.punctuation)).replace(" ","").lower()
        if s == s[::-1]:
            return True
        else: return False