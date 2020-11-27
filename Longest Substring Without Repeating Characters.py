#  Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "#abc$2 "
# Output: 7


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        startindex=0
        presentvalue=0
        len=0
        for letter in s:
            if letter not in dic.keys():
                dic[letter]=0
            
            if(dic[letter]<=startindex):
                dic[letter]=presentvalue+1
                presentvalue+=1
            else:
                startindex=dic[letter]
                dic[letter]=presentvalue+1
                presentvalue+=1

            if((presentvalue-startindex)>len):
                len=presentvalue-startindex
        return len
            
                
