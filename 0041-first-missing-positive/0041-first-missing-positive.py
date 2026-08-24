class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
        largest = max(a)
        if largest < 1:
            return 1
        d = {}


        for i in a:
            if i < 1:
                continue
            d[i] = d.get(i , 0) + 1

        print(d)

        for i in range(1, largest + 2):
            if i not in d.keys():
                return i
         
