import csv
import pandas as pd

rows=[]

with open("star.csv","r") as f :
  data=csv.reader(f)
  for row in data:
    rows.append(row)

header=rows[0]
planetData=rows[1:]

header[0]="Index"

distance=[]

for data in planetData:
    if float(data[2])<100:
        distance.append(data)

print(len(distance))

gravity=[]
for data in planetData:
    if float(data[5])<150 or float(data[5])>350:
        gravity.append(data)

print(len(gravity))

final_list=[]
for data in distance:
    if data in gravity:
        final_list.append(data)


with open("filterd_star.csv","a+") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(final_list)
