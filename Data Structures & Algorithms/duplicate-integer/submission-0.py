class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=[]
        for n in nums:
            if n in s:
                return True
            s.append(n)
        return False
        