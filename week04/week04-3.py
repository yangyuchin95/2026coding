#week04-3.py
#3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ans = -1 #找不到答案就是-1
        N = len(nums) #有N個數
        H = [0] * 200 #有很多格H[??]對應??出現幾次
        for i in range(N):
            H[nums[i]] += 1 #把出現數字塞進H[??]
        #再逐個檢查「偶數」出現幾次
        for i in range(N): #逐一檢查
            if nums[i] % 2 == 0 and H[ nums[i] ] == 1: #偶數才處裡
                return nums[i]
        return ans
