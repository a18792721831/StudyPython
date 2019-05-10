import threading
import time
from HelloThread import thQueue
from HelloThread import dataQueue


class myThread(threading.Thread):
    def __init__(self, threadId, name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name

    def setQueue(self, dataQueue):
        self.dataQueue = dataQueue

    def setLock(self, lock):
        self.lock = lock

    def run(self):
        global thQueue
        global lock
        print('start myThread')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        thQueue.acquire()
        lock.put(self.name)
        thQueue.release()
        time.sleep(2)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('end myThread')