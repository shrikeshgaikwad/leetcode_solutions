class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000 :
            return 0
        
        if len(str(n)) % 3 == 0  :
            return (len(str(n)) // 3 -1) + (n - 1000)
        return len(str(n)) // 3 + n - 1000

        

        