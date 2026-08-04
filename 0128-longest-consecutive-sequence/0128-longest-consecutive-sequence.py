class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        if len(a)== 0:
            return 0
        s = set(a)
        a = list(s)
        a.sort()
        print(s)
        num = 0
        m = 0
        for i in range(len(a)-1):
            if a[i+1] == a[i] + 1:
                num+= 1
            else:
                num = 0 

            if num > m :
                m = num 

        return m + 1 

        