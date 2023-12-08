from threading import Thread
import time
def red():
    while True:
        print("Красный")
        time.sleep(14)
def yellow():
    while True:
        time.sleep(5)
        print("Желтый")
        time.sleep(2)
def green():
    while True:
        time.sleep(7)
        print("Зеленый")
        time.sleep(7)

redlight = Thread(target=red)
yellowlight = Thread(target=yellow)
greenlight = Thread(target=green)
redlight.start()
yellowlight.start()
greenlight.start()