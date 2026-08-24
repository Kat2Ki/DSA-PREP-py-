class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=[]
        for li in s:
            if li.isalnum():
                clean.append(li.lower())

        if clean == clean[::-1]:
            return True
        else:
            return False


         