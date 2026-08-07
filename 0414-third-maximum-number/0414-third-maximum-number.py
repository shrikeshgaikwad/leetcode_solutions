class Solution:
    def thirdMax(self, a: List[int]) -> int:
        first = float("-inf")
        second = float("-inf")
        third =  float("-inf")
 
        for i in range(len(a)):
            print(a[i])
            if a[i] == first or a[i] == second or a[i] == third:
                continue
            if a[i] > first: 
                third = second 
                second = first 
                first = a[i]
            elif a[i] > second : 
                third = second 
                second = a[i]
            elif a[i] > third :
                third = a[i]


        print()
        print(first)
        print(second)
        print(third)

        if third != float("-inf"):
            return third
        return first




        