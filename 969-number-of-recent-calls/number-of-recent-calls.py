class RecentCounter:

    def __init__(self):
        self.queue = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while (t - 3000) > self.queue[self.start]:
            self.start += 1

        return len(self.queue) - self.start
