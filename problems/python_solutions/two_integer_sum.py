from typing import *  # type: ignore


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer. first start from left, second start from after the left.
        # add the two pointers and check if eq to target
        for i, left in enumerate(nums):
            # print("l", left)
            for j, right in enumerate(nums[i+1:]):
                # print('r', right)
                if left + right == target:
                    return [i, j+i+1]

Solution().twoSum([3,4,5,6], 7)
