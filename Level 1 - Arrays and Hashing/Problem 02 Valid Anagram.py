'''
Problem 242 on Leetcode
Rating: Easy

The prompt:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example input: s = "anagram", t = "nagaram"
Expected output: true
'''

import unittest

# These first two lines given by Leetcode
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I initially feel overwhelmed by doing this any other way than sorting both arrays and
        #   checking to see if they're equal.
        # Sorted function uses merge sort, so the time complexity is O(n*log(n))
        # Beats 58.57% of Python users on time, 14.91% on space
        # Had the idea because I saw a comment on a YouTube video yesterday that set to see if
        #   the Contains Duplicates problem could be solved by checking a set of the array
        #   against the original array.
        s = sorted(s)
        t = sorted(t)
        if (s == t):
            return True
        else:
            return False
        
class SolutionTest(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(Solution.isAnagram(Solution, s = "anagram", t = "nagaram"))
        self.assertFalse(Solution.isAnagram(Solution, s = "rat", t = "car"))

unittest.main()

# What did I learn here?
# 1. I almost made the mistake of trying to use an assertEqual test case instead of assertTrue or
#      assertFalse. I need to start with thinking about what the function returns.
# 2. Thinking about if two arrays are equal after sorting or being converted to a set seems to help
#      with quite a few array problems. Based on binomial distribution math, it's come up twice in
#      two questions, so it might be a very common set of methods to solve these.