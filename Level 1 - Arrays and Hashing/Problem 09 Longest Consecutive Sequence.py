'''
Problem 128 on Leetcode
Rating: Medium

The prompt:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example input: nums = [100,4,200,1,3,2]
Expected output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

from typing import List

# I just had to iterate through a series of mistakes here.
# In the future, I would like to visualize my code beforehand to make sure it works instead of
#   waiting for the computer to tell me the error I've made.
# Beats 91.51% of Python3 submissions, took 40 minutes to read issue and code up.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        storedAnswer = 0
        tempAnswer = 0
        for i in range(0, len(nums)):
            if i == 0:
                storedAnswer += 1
                tempAnswer += 1
            else:
                if (nums[i] - nums[i - 1] == 1):
                    tempAnswer += 1
                else:
                    if (tempAnswer >= storedAnswer):
                        storedAnswer = tempAnswer
                    tempAnswer = 1
        if(tempAnswer >= storedAnswer):
            storedAnswer = tempAnswer
        return storedAnswer

'''
Things I've Learned:
1. I'm still making small mistakes. I'm only checking > or <. I'm not checking for >= or <=.
2. I now know I need to sort after converting to a set, and I need to convert the set back to a list if I want to iterate through it.
3. Sometimes I write a condition to store a value in an intermediary data structure, but if that condition is never broken, I don't have code to transfer that value to the final value.
4. I learned that you can't transfer ls.sort() into a variable. It gives back None as its return value.
5. Since this isn't an in-person interview, I can't ask about multiple values in a row being the same as the old value, but that's an edge case I need to consider.
'''