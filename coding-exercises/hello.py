import queue

class Solution:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, item):
        self.q1.put(item)
        while not self.q2.empty():
            self.q1.put(self.q2.get())

        temp = self.q2
        self.q2 = self.q1
        self.q1 = temp

    def pop(self):
        if not self.q2.empty():
            return self.q2.get()

    def empty(self):
        return self.q2.empty()

    def top(self):
        if self.q2.empty():
            return
        return self.q2.queue[0]

s = Solution()
s.push(1)
s.push(2)

print(s.top())
print(s.pop())
print(s.top())