import numpy as np
import pandas as pd
import psutil

print("Monitoring CPU Usage...")

## Specify the threshold
threshold = 80

## Use try catch to handle exceptions
## Declare "While" loop to be true for endless execution
## Use "If" condition to check if cpu_usage_percentage is greater than threshold.
## If yes, print the usage percentage
## In case of exception, print the error message "An error occured"
try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        
        if cpu_usage*100>threshold:
            print(f"Alert! CPU usage exceeds threshold:{cpu_usage*100}%")
except:
    print("An error occured.")

if __name__ == '__main__':
    print("Monitoring CPU Usage...")