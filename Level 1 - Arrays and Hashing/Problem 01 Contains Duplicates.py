'''
Problem 217 on Leetcode
Rating: Easy

The prompt:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example input: nums = [1, 2, 3, 1]
Expected output: true
'''

from typing import List
import unittest

# These first two lines given by Leetcode
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Naive approach: Iterate through list - O(n^2)
        # The count function is O(n), and we are doing that for up to n items
        # This approach failed a latter test for being too slow on an array with 54,500 members
        # for num in nums:
        #     if nums.count(num) > 1:
        #         return True
        #     else:
        #         continue
        #     return False

        # Second approach: Load values into a dictionary as keys, values are counts, if value
        #   is found in dictionary, return True
        # This should be linear - O(n)
        # Beats 11.47% of Python3 users on time, 11.08% on space
        storageDict = {}
        for num in nums:
            if num in storageDict:
                return True
            else:
                storageDict[num] = 1
        return False
        
Solution.containsDuplicate(Solution, nums = [2, 14, 18, 22, 22])

class TestAnswer(unittest.TestCase):
    def test_contains_duplicates(self):
        self.assertTrue(Solution.containsDuplicate(Solution, nums = [1, 2, 3, 1]))
        self.assertFalse(Solution.containsDuplicate(Solution, nums = [1, 2, 3, 4]))
        self.assertTrue(Solution.containsDuplicate(Solution, nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertTrue(Solution.containsDuplicate(Solution, nums = [2, 14, 18, 22, 22]))

unittest.main()

# What did I learn here?
# 1. Pass in the class as a required argument when calling a method
# 2. Import List to use that functionality
# 3. Double-check the expected output and input, I had originally reversed True and False here
# 4. Learned to run unit tests in Python3
# 5. Difference between 'pass' and 'continue'
# 6. Using a dictionary doesn't automatically beat 50% of users in your language