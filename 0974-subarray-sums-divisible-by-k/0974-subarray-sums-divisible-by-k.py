class Solution:
    def subarraysDivByK(self, a: List[int], k: int) -> int:
        cnt = 0
        prefix = 0

        freq = {0: 1}

        for x in a:
            prefix += x

            remainder = prefix % k

            if remainder in freq:
                cnt += freq[remainder]

            freq[remainder] = freq.get(remainder, 0) + 1

        return cnt