import base64
from datetime import datetime

import cv2
# import numpy as np
import pyzbar.pyzbar as pyzbar
# import sys
import time
# import pybase64
import json

import pandas as pd

# start webcam

cap = cv2.VideoCapture(0)

# df = pd.DataFrame(["Name","Entry Time"])
entry_time = []
df = pd.DataFrame(entry_time, columns=["Name", "Entry Time"])



names = []

# function for Attendance file

fob = open('attendance.txt', 'a+')


def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z = "".join(str(z))
        fob.write(z + '\n')
        return names


print('Reading code...........')

with open("records.json", "r+") as records:
    file_data = json.load(records)
    studentDetails = file_data["studentDetails"]


# function data present or not

def checkData(data):
    data = data.decode()
    student_name = studentDetails[data]["name"]
    student_roll = str(studentDetails[data]["roll"])
    if student_name in names:
        print("Roll No. " + student_roll + ": " + student_name + ' is Already Present')
    else:
        entry_time.append([student_name, datetime.now()])
        print('\n' + "Roll No. " + student_roll + ": " + student_name + ' Present done')
        enterData(student_name)


while True:
    _, frame = cap.read()
    decodedObject = pyzbar.decode(frame)
    for obj in decodedObject:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow('Frame', frame)

    # close
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
for i in range(len(entry_time)):
    df = df.append({"Name":entry_time[i][0], "Entry Time":entry_time[i][1]}, ignore_index=True)
# print(entry_time)

print(df)

df.to_csv('attendance.csv')

cv2.destroyAllWindows()


# print(entry_time)

fob.close()
