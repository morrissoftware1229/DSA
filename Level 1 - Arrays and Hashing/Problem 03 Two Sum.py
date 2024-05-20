'''
Problem 1 on Leetcode
Rating: Easy

The prompt:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example input: nums = [2,7,11,15], target = 9
Expected output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Since there's exactly one solution, I'm going to add them to a dictionary, and check
        # the dictionary for the other value to find the indices. If the other value isn't found,
        # I'll check the next one.
        # Time complexity here is O(n).
        # This answer beats 85.12% of Python3 submitted answers on time, 41.58% on space.
        solutionsList = []
        solutionsDict = {}
        for n in range(0, len(nums)):
            if n == 0:
                solutionsDict[nums[n]] = n
            else:
                if (target - nums[n]) in solutionsDict:
                    solutionsList = [solutionsDict[target-nums[n]], n]
                    return solutionsList
                else:
                    solutionsDict[nums[n]] = n
        return [-1, -1]
    
class SolutionTest(unittest.TestCase):
    def testTwoSum(self):
        self.assertEqual(Solution.twoSum(self, nums=[2,7,11,15], target = 9), [0,1])
        self.assertEqual(Solution.twoSum(self, nums=[3,2,4], target=6), [1,2])
        self.assertEqual(Solution.twoSum(self, nums=[3,3], target=6), [0,1])

unittest.main()

# Things I learned:
# 1. I was reminded that in Python loops stop before the last integer in the range type.
# 2. I was reminded to be careful about referencing a key in a dictionary instead of just the integer of the loop.
