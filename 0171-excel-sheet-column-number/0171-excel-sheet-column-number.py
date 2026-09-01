class Solution:
    def titleToNumber(self, a: str) -> int:
        total = 0
        place = 0

        for i in range(len(a) - 1, -1, -1):
            total += (ord(a[i]) - 64) * (26 ** place)
            place += 1

        return total