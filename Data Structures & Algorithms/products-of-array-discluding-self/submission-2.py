class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:])
        return result
        
        
        