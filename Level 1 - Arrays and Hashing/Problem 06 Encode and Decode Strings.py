'''
Problem 271 on Leetcode
Rating: Medium

The prompt:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

Example input: s = "anagram", t = "nagaram"
Expected output: true
'''

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            if(s == ""):
                encodedString = encodedString + ""
            elif(encodedString == ""):
                encodedString = s
            else:
                encodedString = encodedString + " " + s
        return encodedString
        

    def decode(self, s: str) -> List[str]:
        loadingString = ""
        stringList = []
        for letter in s:
            if letter != " ":
                loadingString += letter
            else:
                stringList.append(loadingString)
                loadingString = ""
        stringList.append(loadingString)
        return stringList

print(Codec.decode(Codec, s=Codec.encode(Codec, strs=["Hello","World"])))
# I'm moving on from this because it's turning into a brainteaser instead of a lesson in good
#   DSA practices.

# Things I Learned
# 1. I'm still making simple mistakes. I indent incorrectly. I use a data structure for intermediate
#      steps, and I forget to reset it. I forget to account for how the first step and the final
#      step will be different from other steps. I actually forgot to put a return statement on the
#      second function. I also forgot to account for a list with multiple empty strings.
# 2. I learned about non-ASCII delimiters, escaping, and chunked transfer encoding being used in
#      these contexts. Unfortunately, I tried to use an ASCII delimiter. Because the first example
#      was ["Hello", "World"], I failed to consider ["Hello World"] is also a single string.