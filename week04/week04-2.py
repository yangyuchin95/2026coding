#week04-2.py
#1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain) #陣列長度
        ans = H = 0
        H = 0 #一開始高度0
        for i in range(N): #逐個加起來
            H += gain[i] #現在增減的量gain[i]加進H
            ans = max(ans, H) #更新答案
        return ans
