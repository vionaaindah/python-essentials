class QueueError(IndexError):  # Choose base class for the new exception.
    #  Write code here
    pass


class Queue:
    def __init__(self):
        # Write code here
        self.__queue = []

    def put(self, elem):
        # Write code here
        self.__queue.insert(0, elem)

    def get(self):
        # Write code here
        if len(self.__queue) > 0:
            elem = self.__queue[-1]
            del self.__queue[-1]
            return elem
        else:
            raise QueueError

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
