#week02-3.py
#392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t) #字串長度
        if N1==0: return True #陷阱:如果右邊字串是空的 就不用比了
        i = 0
        for k in range(N2): #右邊一個個試
            if s[i] == t[k]: #找到一個1「左右」符合的
                i += 1 #左邊i往右升一級
        if i==N1: #左邊的i有走到最後結束
            return True
        else: #沒有走到最後
            return False
