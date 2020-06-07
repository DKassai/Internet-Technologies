from threading import Thread
import time
def wait():
    i = 0
    try:
        while True:
            print("tig ol bitties " + str(i))
            i+=1
    except:
        print("I have relieved myself")


t = Thread(target=wait)
t.start()
time.sleep(2)
try:
    exit()
except:
    print("yeehaw")