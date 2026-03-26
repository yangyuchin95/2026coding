#week05-4.py
#3546. Equal Sum Grid Partition I
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row) for row in grid])

        preSum = 0 #對應橫切
        for row in grid: #逐個row處裡
            preSum += sum(row) #row整行加起來
            if preSum == total -  preSum: #上半部==下半部
                return True

        preSum = 0 #對應直切
        for col in zip(*grid):
            preSum += sum(col)
            if preSum == total -  preSum: #上半部==下半部
                return True

        return False
