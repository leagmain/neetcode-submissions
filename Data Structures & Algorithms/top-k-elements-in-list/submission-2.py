class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        return [k for k, _ in cnt.most_common(k)]