#week07-2.py
#735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a>0: #正的往右 不會跟左邊相撞
                ans.append(a) #直接塞
            else:
                while ans and ans[-1]>0: #目前有存 且最右邊正的、向右，會相撞
                    if abs(ans[-1]) == abs(a): #絕對值大小都相同 都消滅
                        ans.pop()
                        a = 0
                        break #離開迴圈
                    elif abs(ans[-1]) > abs(a): #右邊比較小 消滅
                        a = 0
                        break
                    else:
                        ans.pop() #消滅吐掉
                if a != 0: ans.append(a)
        return ans
