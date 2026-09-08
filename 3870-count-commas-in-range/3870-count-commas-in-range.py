class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        if n <= 1000000:
            return n - 999
        
        else:
            return 6
        

        

        