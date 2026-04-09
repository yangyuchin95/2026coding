#week07-6.py
#649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR,banD = 0, 0
        R, D = senate.count('R'), senate.count('D')
        while queue: #進行互相ban對方的遊戲
            now = queue.popleft()
            if now == 'R':
                if banR>0: #已經紀錄要消滅1個人
                    banR -= 1 #用掉1個消滅名額
                    R -= 1 #馬上少1人
                else:
                    banD += 1
                    queue.append(now) #再到最右邊排隊
            else:
                    if banD>0:
                        banD -= 1
                        D -= 1
                    else:
                        banR += 1
                        queue.append(now)

            if R==0: return 'Dire'
            if D==0: return 'Radiant'
