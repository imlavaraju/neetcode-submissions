class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={} #dict
        #nums = [1,2,3]
        #target=3
        for index,num in enumerate(nums):
            complement = target - num
            #eg complement = 3-1=2 ,next iterate 3-2=1
            if complement in seen: #2 not in seen,1 in seen
                return [seen[complement],index]
                #seen[1]=0 and index=1 then return [0,1]
            seen[num] = index
            #seen[1] = 0 means {1:0}
        return []