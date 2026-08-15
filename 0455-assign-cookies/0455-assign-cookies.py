class Solution:
    def findContentChildren(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()

        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if b[j] >= a[i]:
                i += 1

            j += 1

        return i