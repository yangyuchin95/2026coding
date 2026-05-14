#week12-3.py
#547. Number of Provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected) #v先知道有Nodes
        visited = set() #走過的地方不要再走

        def helper(now):
            visited.add(now)
            for k in range(N):
                if k not in visited and isConnected[now][k]:
                    helper(k)
        ans = 0
        for i in range(N): #全部Node巡一次
            if i not in visited: #沒有去過的話
                ans += 1 #代表是新的一群
                helper(i)
        return ans
