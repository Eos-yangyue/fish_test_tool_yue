# 新建两个线程，输入xy，让线程A每x秒输出一下当前时间戳，线程B每y秒输出一下当前时间戳
import _thread
import time
import threading

def print_time(name,delay):
    while True:
        time.sleep(delay)
        print(name,"time.ctime(): %s" % time.ctime())

'''try:
    _thread.start_new_thread(print_time, ("Thread-1", 4,))
    _thread.start_new_thread(print_time, ("Thread-2", 2,))
except:
  print("An exception occurred")
'''
a = input("请输入线程t间隔时间，s为单位：")
b = input("请输入线程t2间隔时间，s为单位：")
t = threading.Thread(target=print_time,args=("Thread-1", int(a),))
t2 = threading.Thread(target=print_time,args=("Thread-2", int(b),))
t.start()
t2.start()

