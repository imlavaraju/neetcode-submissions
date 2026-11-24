class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=[] # as an array
        # s= set()
        for n in nums:
            if n in s:
                return True
            s.append(n)
            #s.add(n) 
        return False
        