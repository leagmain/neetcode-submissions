class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list(nums)
        for i, n in enumerate(nums):
            result[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:])
        return result
        
        
        