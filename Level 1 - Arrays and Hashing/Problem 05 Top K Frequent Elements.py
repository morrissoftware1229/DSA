'''
Problem 347 on Leetcode
Rating: Medium

The prompt:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example input: nums = [1,1,1,2,2,3], k = 2
Expected output: [1,2]
'''

from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I can use a defaultdict to store values, sort by values, and return 0 to k
        # This initial attempt beat 51.16% of Python3 submissions on time
        returnList = []
        intDict = defaultdict(int)
        for n in nums:
            intDict[n] += 1
        sortedIntDict = sorted(intDict.items(), key=lambda v: v[1], reverse=True)
        for val in range(0, k):
            returnList.append(sortedIntDict[val][0])
        return returnList

Solution.topKFrequent(Solution, nums=[1, 1, 1, 2, 2, 3], k=2)

# Things I learned
# 1. How to pass in a lambda function to get a defaultdict sorted by value
# 2. I need to read the editorials in Leetcode to better understand the structures and approaches
# 3. In order to understand the QuickSelect editorial, I had to refresh my understanding of sorting
#      algorithms. Bubble sort compares two items at a time and makes multiple loops through an array.
#      O(n^n). Quicksort pickes a randomly chosen item, a "pivot", and compares all other items to it.
#      The compared items are moved to the right if they are "greater" than the compared item. This
#      would also be O(n^n) but with a better average time. Merge sort is O(n log(n)). I can recall
#      from my algorithms class how insertion sort works, and that is also O(n^n).
# 4. QuickSelect is also referred to as Hoare's sorting algorithm.
# 5. I learned what Lomuto's Partitioning Scheme was and that partitioning schemes are extremely
#      important in parallel algorithms.