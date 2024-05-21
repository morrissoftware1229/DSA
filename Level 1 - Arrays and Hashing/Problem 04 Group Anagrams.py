'''
Problem 49 on Leetcode
Rating: Medium

The prompt:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example input: strs = ["eat","tea","tan","ate","nat","bat"]
Expected output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

from typing import List
# from collections import Counter
from collections import defaultdict
import unittest

# These first two lines given by Leetcode
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # My first thought was to convert all values to their ASCII equivalent and sum them,
        #   but two 16s would also sum to 32, so it could easily break.

        # My next though is to check each value against other values using the built-in counter
        #   function I learned about in problem 02. This would get it down to a time complexity
        #   of O(n^2), but I wonder if I can do better than that.

        # finalList = []
        # loadingList = []
        # for s in strs:
        #     loadingList.append(s)
        #     for t in strs:
        #         if (s == t):
        #             continue
        #         elif (Counter(s) == Counter(t)):
        #             loadingList.append(t)
        #     # Currently, I'm having to make sure my anagram group isn't already in because I don't
        #     #   know how to eloquently remove those values without breaking the loop or making the
        #     #   code hard to read.
        #     if(len(finalList) == 0):
        #         finalList.append(loadingList)
        #     else:
        #         for f in finalList:
        #             if loadingList not in finalList:
        #                 finalList.append(loadingList)
        #             else:
        #                 continue
        # return finalList
    # I've spent more than an hour looking at this, so I will check the solutions and move on.

        # This is the best performing solution for Python3 for time complexity that doesn't
        #   circumvent the purpose of learning algorithms
        anagram_map = defaultdict(list)
        result = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        for items in anagram_map.values():
            result.append(items)
        return result

Solution.groupAnagrams(Solution, strs=["eat", "tea", "tan", "ate", "nat", "bat"])


# Things I learned
# 1. Don't forget to extrapolate out unforeseen edge cases. My ASCII approach made sense because
#      I saw examples with only three letters. It may not work as well with seven-letter words.
# 2. I've made two mistakes. First, I didn't check to see if make sure I wasn't comparing a string
#      against itself, so I initially had "eat" and "eat" loading into an intermediate list. Second,
#      I tried to access the list I return with nothing in it. "For f in returnList" won't work if
#      there aren't yet any values in returnList.
# 3. Defaultdict doesn't require you to set an initial value for a dictionary key, so it can be used
#      much more intuitively.
# 4. This problem basically came down to checking to make sure a series of strings contained the same
#      characters, so sorting the strings without changing the underlying values was very helpful.
# 5. Though I try not to iterate through loops multiple times, it was extremely helpful in this
#      solution. I should do things in multiple steps if necessary.
