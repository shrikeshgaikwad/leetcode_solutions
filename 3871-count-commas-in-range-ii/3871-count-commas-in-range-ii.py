class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000 :
            return 0
        commas = 0
        power = 1000

        while power <= n:
            commas += (n - power +1)
            power *= 1000
        
        return commas
        