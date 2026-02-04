class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        range = t - 3000
        if range <= 0:
            self.queue.append(t)
        elif self.queue and range <= self.queue[0]:
            self.queue.append(t)
        else:
            while self.queue and range > self.queue[0]:
                self.queue.pop(0)
            self.queue.append(t)
        return len(self.queue)
