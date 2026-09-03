class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        left=0
        max_len=0

        for right in range(len(s)):
            #if duplicate in the window shrink the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1

            #add current character in the window
            char_set.add(s[right])

            #update the maximum length
            max_len=max(max_len, right-left+1)
        
        return max_len