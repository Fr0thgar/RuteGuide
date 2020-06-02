from sense_hat import SenseHat
from datetime import datetime
from time import sleep

import csv
from csv import writer

FILENAME = ''
WRITE_FREQUENCY = 100
sense = SenseHat()
timestamp = datetime.now()
delay = 1 
blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

batch_data = []

## Function ##
def file_setup(filename):
    header = ['acc_x', 'acc_y', 'acc_z', 'datetime']

    with open(filename, 'w') as f:
        f.write(','.join(str(value) for value in header)+ '\n')

def log_data():
    output_string = ','.join(str(value) for value in sense_data)
    batch_data.append(output_string)

def get_sense_data():
    sense_data = []
    sense_data.append(sense.get_accelerometer_raw())
    
    accelerometer = sense.get_accelerometer_raw()
    sense_data.append(accelerometer['x'])
    sense_data.append(accelerometer['y'])
    sense_data.append(accelerometer['z'])

    sense_data.append(datetime.now())

    return sense_data

## Main Program ##

if FILENAME == '':
    filename = 'SenseLog-'+str(datetime.now())+'.csv'
else:
    filename = FILENAME+'-'+str(datetime.now())+'.csv'

file_setup(filename)
while True:
    sense_data = get_sense_data()
    log_data()
    acc = sense.get_accelerometer_raw()
    x = acc['x']
    y = acc['y']
    z = acc['z']

    
    if x > 1.2 or y > 1.2 or z > 1.2:
        print('Writing to file..')
        with open(filename, 'a') as f:
            for line in batch_data:
                f.write(line + '\n')
            batch_data = []



