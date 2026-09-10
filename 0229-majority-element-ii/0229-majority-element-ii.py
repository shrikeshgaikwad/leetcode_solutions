class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        d = len(a) / 3
        ans = []

        b = {}

        for i in a:
            b[i] = b.get(i, 0) + 1
        
        for i in b.keys():
            if i in ans:
                continue
            if b[i] > d:
                ans.append(i)
        return ans