class Solution:
    def missingMultiple(self, a: List[int], k: int) -> int:
        largest = max(a)

        for i in range(k, largest + 2*k, k):
            if i not in a:
                return i
        
        return -1