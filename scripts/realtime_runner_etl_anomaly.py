import subprocess
import time

while True:
    subprocess.call(['python', 'scripts/etl_pipeline.py'])
    subprocess.call(['python', 'scripts/anomaly_detection.py'])
    print("[INFO] ETL + Anomaly run completed.")
    time.sleep(15)  # wait 15 seconds, then check for new records again
