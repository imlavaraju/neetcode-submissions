from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count = Counter(nums)

        result = sorted(count, key=count.get, reverse=True)

        return result[:k]