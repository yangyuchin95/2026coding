#week07-5.py
#933. Number of Recent Calls
class RecentCounter:

    def __init__(self):
        #使用Queue的資料結構 但python有collections.deque
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t) #從右邊塞入1個數
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
