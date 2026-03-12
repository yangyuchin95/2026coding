#week03-2.py
#643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums) #陣列的長度
        total = sum( nums[:k] ) #加總[:k] 前k項
        maxTotal = total
        for i in range(k, N):
            total = total + nums[i] - nums[i-k]
            #nums[i]右邊的頭(往右),nums[i-k]左邊的尾吐出來
            maxTotal = max(maxTotal, total)
        return  maxTotal/k
