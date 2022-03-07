import time
from plyer import notification

def notify():
    while True:
      notification.notify(
        title="*Alert Motion Detected*!!",
        message = "Check Your Belongings",
        app_icon = "alert.ico",
        timeout = 5
      )
      time.sleep(10*10)


notify()

