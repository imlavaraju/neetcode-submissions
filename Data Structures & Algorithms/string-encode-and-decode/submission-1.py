class Solution:

    def encode(self, strs: List[str]) -> str:
        string=str()
        for s in strs:
            string = string + str(len(s)) + "#" + str(s)
        print(string)
        return string



    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i < len(s):
            j = i

            while s[j] != "#":
                j=j+1
            length = int(s[i:j])
            word = s[j+1 :length+j+1]
            result.append(word)
            i=j+1+length
        return result

