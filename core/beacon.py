import requests
import time

def send_beacon(master_url):
    while True:
        try:
            requests.post(f"{master_url}/status")
        except:
            pass
        time.sleep(300) # Heartbeat interval
