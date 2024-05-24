'''
Problem 238 on Leetcode
Rating: Medium

The prompt:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example input: nums = [1,2,3,4]
Expected output: [24,12,8,6]
'''

import unittest
from typing import List
from collections import defaultdict

# First two lines given by Leetcode
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The intuitive answer here is to loop through for each value, but that's O(n^n)
        # I could instead add them to a defaultdict using the integer as key and do the math on the
        #   element. That would be O(n).
        answerDict = defaultdict(int)
        # While I don't want to, I can't immediately think of how to not loop through twice
        # This is only hard because I can't use the division operator
        # I have an idea. I can use the index as the key instead and load them into a list in order.
        for n in range(0, len(nums)):
            answerDict[n] = 1
        for n in range(0, len(nums)):
            # Multiply all values where key does not match by other values
            if (n != answerDict.keys[n]):
                answerDict[n] *= nums[n]
            else:
                # Zen of Python - Explicit is better than implicit
                continue
        answer = answerDict.values()
        return answer
    
# What I've Learned
# 1. I really need to brush up on how to access elements in a dictionary. That is what's really
#      holding me back on these.
# 2. The editorial solution comes down to the associative property of multiplication. I could have
#      initialized three arrays - answer, left of index, and right of index. Then, I could have
#      looped through from left to right and also from right to left, and I could have multiplied
#      the product to the left of the index times the product to the right of the index to get the
#      answer for each index. 
