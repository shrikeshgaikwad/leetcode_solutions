class Solution:
    def pivotIndex(self, a: List[int]) -> int:

        n = len(a)

        sumLeft = [0] * n
        sumRight = [0] * n

        # Prefix sums
        for i in range(1, n):
            sumLeft[i] = sumLeft[i-1] + a[i-1]

        # Suffix sums
        for i in range(n-2, -1, -1):
            sumRight[i] = sumRight[i+1] + a[i+1]

        print(sumLeft)
        print(sumRight)

        for i in range(n):
            if sumLeft[i] == sumRight[i]:
                return i

        return -1