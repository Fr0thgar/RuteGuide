from sense_hat import SenseHat
from datetime import datetime
import csv
from csv import writer


sense = SenseHat() 
timestamp = datetime.now() 
delay = 1

def get_sense_data():
    sense_data = []
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_pressure())
    sense_data.append(sense.get_humidity())

    orientation = sense.get_orientation()
    sense_data.append(orientation['yaw'])
    sense_data.append(orientation['pitch'])
    sense_data.append(orientation['roll'])
    
    mag = sense.get_compass_raw()
    sense_data.append(mag['x'])
    sense_data.append(mag['y'])
    sense_data.append(mag['z'])

    gyro = sense.get_gyroscope_raw()
    sense_data.append(gyro['x'])
    sense_data.append(gyro['y'])
    sense_data.append(gyro['z'])

    acc = sense.get_accelerometer_raw()
    sense_data.append(acc['x'])
    sense_data.append(acc['y'])
    sense_data.append(acc['z'])

    sense_data.append(datetime.now())
    
    return sense_data

with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp', 'pres', 'hum',
    'yaw','pitch', 'roll',
    'mag_x', 'mag_y', 'mag_z',
    'acc_x', 'acc_y', 'acc_z',
    'gyro_x', 'gyro_y', 'gyro_z',
    'datetime'])

    while True:
        print(get_sense_data())
        data = get_sense_data()
        dt = data[-1] - timestamp 
        if dt.seconds > delay:
            data_writer.writerow(data)
            timestamp = datetime.now()



    