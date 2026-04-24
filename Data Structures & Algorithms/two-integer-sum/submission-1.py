class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_2_i = {}
        
        for i in range(len(nums)):
            nj = target - nums[i]
            if nj in n_2_i:
                return [n_2_i[nj], i]
            n_2_i[nums[i]] = i

        return []
        

