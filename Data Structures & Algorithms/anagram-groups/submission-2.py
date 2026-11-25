
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            key = tuple(count) #array or list cant be a key of dict so changing into tuple
            if key not in anagram:
                anagram[key]=[]

            
            anagram[key].append(word)
        return list(anagram.values())
      


        