"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

date_filtered = list(filter(lambda x: x[2][3:10]=='09-2016',calls))
dic = dict()
for row in date_filtered:
    if row[0] in dic:
        dic[row[0]] += int(row[3])
    else:
        dic[row[0]] = int(row[3])
    if row[1] in dic:
        dic[row[1]] += int(row[3])
    else:
        dic[row[1]] = int(row[3])

lon = max(dic,key=lambda x: dic[x])
print(f"{lon} spent the longest time, {dic[lon]} seconds, on the phone during September 2016.")
