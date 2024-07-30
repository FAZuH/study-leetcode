from typing import *  # type: ignore


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map: dict[int, int] = {}
        """Mapping number to frequency"""

        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)

        return [e[0] for e in sorted(freq_map.items(), key=lambda x: x[1], reverse=True)][:k]


class NeetSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return []


obj = Solution()
ret = obj.topKFrequent([1,2,2,3,3,3], 2)
print(ret)
