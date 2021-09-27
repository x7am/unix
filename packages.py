import time
from datetime import datetime

def current_time():
    print('Time Now -'+' ['+time.strftime("%H:%M:%S", time.localtime())+']')


    