
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ref = strs[0]
        prf = ""

        for i in range(len(ref)):
            char = ref[i]

            for strings in strs:
                if i >= len(strings) or strings[i] != char:
                    return prf

            prf += char

        return prf
