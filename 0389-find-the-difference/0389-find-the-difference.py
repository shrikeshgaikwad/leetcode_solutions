class Solution:
    def findTheDifference(self, a: str, b: str) -> str:
        suma = 0 
        sumb = 0 

        for i in a:
            suma += ord(i)
        for i in b:
            sumb += ord(i)

        return chr(sumb - suma)
        