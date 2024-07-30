from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occured: set[int] = {nums[0]}
        for n in nums[1:]:
            if n in occured:
                return True
            occured.add(n)
        return False
         
