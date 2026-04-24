class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_2_i = {}
        
        for i, ni in enumerate(nums):
            nj = target - ni
            if nj in n_2_i:
                return [n_2_i[nj], i]
            n_2_i[ni] = i

        return []
        

