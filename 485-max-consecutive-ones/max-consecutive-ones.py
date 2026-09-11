class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        max= 0 

        for i in range (len(nums)):
            if nums[i] == 1:
                k=k+1

                if k > max:
                    max = k
            else:
                k = 0
        return max            


        