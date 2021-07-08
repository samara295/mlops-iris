from datetime import datetime

def currenttime():
    now = datetime.now() # current date and time

    time = now.strftime("%H:%M:%S")
    return time
