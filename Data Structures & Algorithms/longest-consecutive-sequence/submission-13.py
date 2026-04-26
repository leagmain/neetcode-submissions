class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        longest = 0
        for n in uniques:
            if n - 1 not in uniques:
                length = 1
                while (n + length) in uniques:
                    length += 1
                longest = max(length, longest)
        return longest
            
            