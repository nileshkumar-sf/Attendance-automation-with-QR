import json

from MyQR import myqr
import os
import base64

# create and read
f = open('student.txt', 'r')
lines = f.read().split("\n")
print(lines)

roll = 1
for i in range(0, len(lines)):
    data = lines[i].encode()
    name = base64.b64encode(data)
    path = "QRCodes/" + lines[i]
    if not os.path.exists(path):
        os.makedirs(path)

    version, level, qr_name = myqr.run(
        str(name),
        level='H',
        version=1,

        # background

        # picture='a.jpg',
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=str(lines[i] + '.bmp'),
        # save_dir=""+"QRIDRecords"+"/"+lines[i]
        save_dir=f"QRCodes/{lines[i]}"
    )

    name = str(name)
    data = {
        "roll": roll,
        "name": lines[i]
    }
    with open("records.json", "r+") as records:
        file_data = json.load(records)
        file_data["studentDetails"][name] = data
        records.seek(0)
        json.dump(file_data, records, indent=4)

    roll += 1
