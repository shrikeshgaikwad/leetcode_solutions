from collections import Counter

class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        count = Counter(a)
        result = []

        for num in b:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result