#week12-4.py
#1466. Reorder Routes to Make All Paths Lead to the City Zero
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set() #走過的不要再走
        ans = 0
        path = defaultdict(list)
        for a, b in connections:
            path[a].append((b, +1))
            path[b].append((a, -1))

        def helper(now):
            ans = 0
            visited.add(now)
            for k,d in path[now]: #城市now可以到城市k，方向是d
                if k not in visited:
                    if d==+1:ans += 1 #驗測方向 若方向出錯+1
                    ans += helper(k)
            return ans
        return helper(0)
