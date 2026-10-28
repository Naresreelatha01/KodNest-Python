from threading import current_thread
import threading
import time
balance=1000
lock=threading.Lock()
def withdraw(amount):
    global balance
    with lock:
        current_balance=balance
        time.sleep(0.1)
        balance = current_balance - amount
        print(f"Thread name =  {current_thread().name}, Balance after withdraw: {balance}")
t1=threading.Thread(target=withdraw, args=(500,))
t2=threading.Thread(target=withdraw, args=(300,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Final Balance:",balance)
   