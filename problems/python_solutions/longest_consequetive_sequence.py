from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))
        longest = 1

        curr = 1
        for i, n in enumerate(sorted_nums[1:]):
            if n - 1 == sorted_nums[i]:
                curr += 1
                if curr > longest:
                    longest = curr
            else:
                curr = 1
        return longest


class NeetSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


obj = Solution()
ret = obj.longestConsecutive([0,3,2,5,4,6,1,1])
print(ret)
