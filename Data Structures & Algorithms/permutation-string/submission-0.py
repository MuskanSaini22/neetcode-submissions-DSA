class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        freq_s1=[0]*26
        freq_window=[0]*26

        for c in s1:
            freq_s1[ord(c)-ord('a')]+=1
        
        for i in range(len(s1)):
            freq_window[ord(s2[i])-ord('a')]+=1

        if freq_window==freq_s1:
            return True
        
        for i in range (len(s1), len(s2)):
            freq_window[ord(s2[i])-ord('a')]+=1
            freq_window[ord(s2[i-len(s1)])-ord('a')]-=1

            if freq_window==freq_s1:
                return True
        return False
