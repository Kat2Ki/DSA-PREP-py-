class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        n = abs(x)
        revn = 0

        while n > 0:
            lastd = n % 10
            revn = revn * 10 + lastd
            n = n // 10
        rev_sign = revn * sign

        if rev_sign < -2147483648 or rev_sign > 2147483647:
            return 0

        return rev_sign

obj = Solution()
num = -123
print(obj.reverse(num))
