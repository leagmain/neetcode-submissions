class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        heap = []
        for _, n in enumerate(count):
            heapq.heappush(heap, (count[n], n))
        return [n for _, n in heapq.nlargest(k, heap)]
