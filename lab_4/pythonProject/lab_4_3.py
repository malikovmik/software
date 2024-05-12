import datetime
import time

def prog_time():
    for _ in range(5):
        current_time = datetime.datetime.now()
        print("Текущее время: ", current_time.strftime("%H:%M:%S"))
        time.sleep(1)

if __name__=='__main__':
    prog_time()