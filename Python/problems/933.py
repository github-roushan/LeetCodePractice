from queue import deque

class RecentCounter:
    def __init__(self):
        self.req = deque()

    def ping(self, t: int) -> int:
        self.req.append(t)
        while self.req[0] + 3000 < self.req[-1]:
            self.req.popleft()
        return len(self.req)
