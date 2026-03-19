#week04-5.py
#724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums) #陣列長度
        prefix = [0] #一開始prefix sum 只有一個0
        for i in range(N):
            prefix.append( prefix[-1] + nums[i] ) #陣列變長

        #print(prefix)
        postfix = [0]*(N+1)
        for i in range(N-1, -1, -1):
            postfix[i] = postfix[i+1] + nums[i]
        for i in range(N):
            if prefix[i] == postfix[i+1]: return i
        return -1
