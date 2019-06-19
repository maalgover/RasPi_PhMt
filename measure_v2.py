#RasPi PhMt

#Libraries
import Rpi.GPIO as GPIO
import time
import Adafruit_ADS1x15
import os
import datetime
import sys

#Variables and flags
GAIN = 1
total_time = input("Total time to measure (hrs): ")
interval = input("Measurement intervals (min): ")
batch_name = input ("Batch ID (max 3 contiguous letters): ")

#Internal parameters setup
measurement = 0
adc = Adafruit_ADS1x15.ADS1115()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

filename = "/home/pi/" + batch_name + ".csv"
file = open (filename, "a")
if os.stat(filename).st_size == 0:
    file.write("Date,Time,Sensor_1\n")
    file.flush()
    file.close()

#Logging
start_time = datetime.now()

while remaining_time.seconds/3600 < total_time:
    GPIO.output(18, GPIO.HIGH)
    sleep(1)
    measurement = adc.read_adc(0, gain=GAIN)
    GPIO.output(18, GPIO.LOW)
    timestamp = datetime.now()
    remaining_time = timestamp-start_time
    file = open (filename, "a")
    file.write(date.isoformat(timestamp.date())+","+time.isoformat(timestamp.time())+","+measurement+"\n")
    file.flush()
    file.close()
    print("Measurement taken")
    sleep(interval*60-1)

print("Measurements finished")
raw_input ("Press any key to terminate")
sys.exit()


