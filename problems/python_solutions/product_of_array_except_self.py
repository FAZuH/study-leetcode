from typing import *  # type: ignore


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [
            self.product(nums[:i] + nums[i+1:])
            for i, _ in enumerate(nums)
        ]

    def product(self, nums: List[int]) -> int:
        ret = nums[0]
        for n in nums[1:]:
            ret *= n
        return ret


class NeetSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res       


from timeit import timeit

# Create instances of the classes
obj = Solution()
obj2 = NeetSolution()

# Test inputs
test_input1 = [1, 2, 4, 6]
test_input2 = [-1, 0, 1, 2, 3]

# Print the results to verify correctness
print(obj.productExceptSelf(test_input1))
print(obj.productExceptSelf(test_input2))

print(obj2.productExceptSelf(test_input1))
print(obj2.productExceptSelf(test_input2))

# Define wrapper functions to measure the execution time
def test_solution():
    obj.productExceptSelf(test_input1)
    obj.productExceptSelf(test_input2)

def test_neet_solution():
    obj2.productExceptSelf(test_input1)
    obj2.productExceptSelf(test_input2)

# Measure execution time using timeit
time_solution = timeit(test_solution, number=10000)
time_neet_solution = timeit(test_neet_solution, number=10000)

print(f"My solution execution time: {time_solution}")
print(f"NeetSolution execution time: {time_neet_solution}")
