#week02-5.py
#1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() #小到大排好 左邊挑一個 右邊挑一個
        ans = 0
        i, j = 0, len(nums) - 1 #最左邊i最小 右邊j對應最大
        while i < j: #還沒有撞在一起 可以左右各挑一個
            if nums[i]+nums[j] == k:
                ans += 1
                i, j = i+1, j-1 #右邊用了 往右 右邊用了 往左
            if nums[i]+nums[j] < k: #加起來太小了 左邊小的i往右移
                i = i+1
            if nums[i]+nums[j] > k: #加起來太大了 右邊小的j往右移
                j = j-1
        return ans
