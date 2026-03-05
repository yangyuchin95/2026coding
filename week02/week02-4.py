#week02-4.py
#11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1 #左邊i 右邊j
        ans = 0
        while i<j: #只要左右沒撞在一起
            area = (j-i) * min(height[i], height[j]) #算出現在的面積
            ans = max(ans, area) #更新答案
            if height[i] < height[j]: i += 1
            else: j -= 1 #小的j往左
        return ans
