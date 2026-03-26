#week05-6.py
#2352. Equal Row and Column Pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter() #Hush map可知道有哪些row出現幾次

        for row in grid:
            #tuple()把陣列[3,1,2,2]變不會動(3,1,2,2)
            counter[tuple(row)] += 1

        ans = 0 #有幾組通過?
        for col in zip(*grid): #矩陣transpose再取出col
            ans += counter[tuple(col)]
        return ans
