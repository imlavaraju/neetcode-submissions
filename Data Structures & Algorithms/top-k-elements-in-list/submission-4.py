from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        result=[]
        for num,freq in count.items():
            buckets[freq].append(num) #time o(n)
        for freq in range(len(buckets)-1,0,-1): #reverse traversal
            for num in buckets[freq]:
                result.append(num)
            if len(result) == k :
                return result 
        # result = sorted(count,reverse=True,key=count.get)
        # return result[:k]


        

        