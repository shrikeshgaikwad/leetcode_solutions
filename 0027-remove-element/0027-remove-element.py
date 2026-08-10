class Solution:
    def removeElement(self, a: List[int], val: int) -> int:
        for i in a[:]:
            if i == val:
                a.remove(i)

        return len(a)