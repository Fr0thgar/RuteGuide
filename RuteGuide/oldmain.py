from sense_hat import SenseHat
from datetime import datetime

import csv
from csv import writer

sense = SenseHat()
timestamp = datetime.now()
delay = 1 
blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

def get_sense_data():
    sense_data = []
    sense_data.append(sense.get_accelerometer_raw())
    
    accelerometer = sense.get_accelerometer_raw()
    sense_data.append(accelerometer['x'])
    sense_data.append(accelerometer['y'])
    sense_data.append(accelerometer['z'])

    sense_data.append(datetime.now())

    return sense_data

with open('data.txt', mode='w', newline='') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['acc_x', 'acc_y', 'acc_z', 'datetime'])

        while True:
            data = get_sense_data()
            acc = sense.get_accelerometer_raw()
            x = acc['x']
            y = acc['y']
            z = acc['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)
            if x > 1.2 or y > 1.2 or z > 1.2:
                sense.show_letter('!', red)
                print(data)
            
                dt = data[-1] - timestamp
                if dt.seconds > delay:
                    data_writer.writerow(data)
                    timestamp = datetime.now()
            else:
                sense.clear()
        
