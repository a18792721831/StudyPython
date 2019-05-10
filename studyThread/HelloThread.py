from MyThread import myThread
import time
import threading
import queue

myth1 = myThread(1520125 ,'myth1')
myth2 = myThread(1214564 ,'myth2')
myth3 = myThread(5441554 ,'myth3')
thQueue = threading.Lock()
dataQueue = queue.Queue(10)
myth1.setQueue(dataQueue)
myth1.setLock(thQueue)
myth2.setQueue(dataQueue)
myth2.setLock(thQueue)
myth3.setQueue(dataQueue)
myth3.setLock(thQueue)
myth1.start()
myth2.start()
myth3.start()
myth1.join()
myth2.join()
myth3.join()
print(dataQueue.qsize())
while not dataQueue.empty():
    print(dataQueue.get())