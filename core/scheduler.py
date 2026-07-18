import schedule
import time
import threading

def maintenance_task():
    print("Automated maintenance sequence executed.")

def run_scheduler():
    schedule.every(1).hour.do(maintenance_task)
    while True:
        schedule.run_pending()
        time.sleep(60)

threading.Thread(target=run_scheduler, daemon=True).start()
