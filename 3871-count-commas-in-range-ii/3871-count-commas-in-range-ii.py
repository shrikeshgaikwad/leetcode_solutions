class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        power = 1000

        while power <= n:
            commas += (n - power +1)
            power *= 1000
        
        return commas
        