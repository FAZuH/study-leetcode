from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate strs, and check if anagram for all in ret.
        # if is anagram, add
        ret: list[list[str]] = [[strs[0]]]
        for s in strs[1:]:
            for t in ret:
                if self.isAnagram(s, t[0]):
                    t.append(s)
                    break
            else:
                ret.append([s])
        return ret

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        countS, countT = {}, {}
        for i in range(len(s)):
            # Genius!
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


class NeetSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
