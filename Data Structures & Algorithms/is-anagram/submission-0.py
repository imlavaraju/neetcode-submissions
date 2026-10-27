class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns,nt=len(s),len(t)
        if ns != nt:
            return False
        s=sorted(s)
        t=sorted(t)
        for i in range(ns):
            if s[i] != t[i]:
                return False
        return True

        