class Solution:
    def generate(self, n: int) -> List[List[int]]:
        a = []
        for i in range(n):
            a.append([0]*(i+1))
        print(a)
        
        for i in range(n):
            for j in range(i+1):
                if j == 0 or j == i: 
                    a[i][j] = 1
                
                else:
                    a[i][j] = a[i-1][j-1] + a[i-1][j]

        return a
        