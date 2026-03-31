import os
import shutil
import time
import datetime

# --- ArmstrongLogic Configuration ---
LOG_PATH = os.path.expanduser("~/Library/Logs/Sentinel/heartbeat.log")
DISK_THRESHOLD_GB = 10  # Critical Fault Trigger

def check_system_vitals():
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "[ArmstrongLogic Online]"
    
    if free_gb < DISK_THRESHOLD_GB:
        log_entry = f"{status} {timestamp} | CRITICAL FAULT: Disk Space at {free_gb}GB. Initiating Sentinel Shield.\n"
        # Add auto-cleanup logic here in future iterations
    else:
        log_entry = f"{status} {timestamp} | Vitals Nominal: {free_gb}GB Free. Heartbeat Active.\n"
    
    with open(LOG_PATH, "a") as f:
        f.write(log_entry)

if __name__ == "__main__":
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    while True:
        check_system_vitals()
        time.sleep(300)  # 5-minute pulse
