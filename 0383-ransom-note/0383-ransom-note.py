class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = {}
        b = {}

        for i in ransomNote:
            a[i] = a.get(i, 0) + 1
        for i in magazine:
            b[i] = b.get(i, 0) + 1
        
        for i in a.keys():
            try:

                if a[i] > b[i]:
                    return False
            except KeyError:
                return False
        return True 