class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        
        a = set(a)
        b = set(b)
        c = list(a.intersection(b))
        return c
        