import time

def red():
    print("Красный")
def yellow():
    print("Желтый")
def green():
    print("Зеленый")
def traficlight():
    while True:
        red()
        time.sleep(5)
        yellow()
        time.sleep(2)
        green()
        time.sleep(5)
        yellow()
        time.sleep(2)
traficlight()