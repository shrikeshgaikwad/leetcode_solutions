class Solution:
    def getRow(self, n: int) -> List[int]:
        a = [] 
        for i in range(n+1):
            a.append([0]* (i + 1))

        for i in range(n+1):
            for j in range(i+1):
                if j == 0 or j == i:
                    a[i][j] = 1 
                else :
                    a[i][j] = a[i-1][j-1] + a[i-1][j]
        
        return a[n]

        