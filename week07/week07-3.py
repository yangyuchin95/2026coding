#week07-3.py
#2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for c in s: #逐一取出字母c再判斷
            if c=='*': ans.pop() #*吐掉一個字母
            else: ans.append(c) #把不是星號的塞回去
        return ''.join(ans) #用單單.join() 把陣列join成字串
