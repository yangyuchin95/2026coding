#week12-1a.py
#841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0] #利用stack裡面有待處理的房間，一開始房間0是開的
        visited =  set() #有去過、處理過不要再進去
        visited.add(0) #已經排好、等待處理，下次拿到鑰匙，不要再放入stack
        while stack: #只要stack還有東西就繼續處理
            now = stack.pop() #吐出1個房間，現在處理
            for k in rooms[now]: #把room now房間哩，所有鑰匙k都拿來檢查
                if k in visited: continue #鑰匙K對應房間k看過了
                stack.append(k) #加入stack資料結構
                visited.add(k) #標記這裡也待處理，其他人不要再排處理
        return len(rooms) == len(visited) #房間數目全部參觀過，成功
