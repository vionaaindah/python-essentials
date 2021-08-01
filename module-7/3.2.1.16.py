class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
       # Write code here
        self.queue = []

    def put(self,elem):
        # Write code here
        self.queue.insert(0, elem)

    def get(self):
        # Write code here
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

class SuperQueue(Queue):
    def isempty(self):
        if not self.queue:
            return True
        else:
            return False

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
