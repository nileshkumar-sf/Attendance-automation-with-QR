import base64

import cv2
# import numpy as np
import pyzbar.pyzbar as pyzbar
# import sys
import time
# import pybase64
import json

# start webcam

cap = cv2.VideoCapture(0)

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

cv2.destroyAllWindows()

fob.close()
