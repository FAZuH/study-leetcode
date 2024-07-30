class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        lettercount_s = { }
        lettercount_t = { }
        for ls, lt in zip(s, t):
            if ls not in lettercount_s:
                lettercount_s[ls] = 0
            else:
                lettercount_s[ls] += 1

            if lt not in lettercount_t:
                lettercount_t[lt] = 0
            else:
                lettercount_t[lt] += 1

        for k, v in lettercount_s.items():
            if k not in lettercount_t or lettercount_t[k] != v:
                return False
        return True


class NeetSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


Solution().isAnagram("abc", "bca")
