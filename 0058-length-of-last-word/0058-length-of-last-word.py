class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) < 1 :
            return 0
        if len(s) == 1 and s[0] != " ":
            return 1
        if len(s) == 1 and s[0] == " ":
            return 0 
        cnt = 0 
        for i in range(len(s),0,-1):
            if s[i-1] == " ":
                continue
            cnt += 1 
            if s[i-2] == " ":
                break
        return cnt