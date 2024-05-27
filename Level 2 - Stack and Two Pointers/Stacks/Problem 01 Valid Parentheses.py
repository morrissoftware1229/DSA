'''
Problem 20 on Leetcode
Rating: Easy

The prompt:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example input: s = "()[]{}"
Expected output: true
'''

# I would first ask if these can be nested. If they can, using a stack makes much more sense to me.
# My first attempt failed to account for a single bracket or empty string.
#   Luckily, the constraints sections says it will not be empty, so we will fail it if the length
#     is not divisible by 2.
# My second attempt failed due to failing to account for a single right bracket.
# My third attempt failed due to failing to account for two left parentheses.
# My fourth attempt passed beating 73.48% of Python3 submissions on time complexity. This is O(n).
#   Though that seems like suboptimal performance, the highest answer is a more concise but less
#     readable version of this answer.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if (p in ["(", "[", "{"]):
                stack.append(p)
            elif (p == ")"):
                if (len(stack) == 0 or stack[-1] != "("):
                    return False
                else:
                    stack.pop()
            elif (p == "]"):
                if (len(stack) == 0 or stack[-1] != "["):
                    return False
                else:
                    stack.pop()
            elif (p == "}"):
                if (len(stack) == 0 or stack[-1] != "{"):
                    return False
                else:
                    stack.pop()
        if (len(stack) != 0):
            return False
        return True
    
'''
Things I've Learned:
1. I need to first think about what could go wrong and do test-driven development. I made three mistakes here not anticipating what inputs could make my output incorrect.
2. The constraints can be useful for letting you know what inputs aren't allowed. Here, the length of the input must be at least 1, so I know I don't have to worry about an empty string.
'''