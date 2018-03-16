import pandas as pd
import os
import datetime

cwd = os.getcwd()
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_data_subset.csv")
#delay_times contains the supervisor district as the key and the delay as the value
#district_freq contains the supervisor district as the key and the number of times that supervisor district is called as the value
delay_times = {}
district_freq = {}

for i in range(len(dataSet['dispatch_timestamp'])):
    print(i)
    if not pd.notnull(dataSet['dispatch_timestamp'][i]) or not pd.notnull(dataSet['supervisor_district'][i]):
        continue
    dispatch = datetime.datetime.strptime(dataSet['dispatch_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    received = datetime.datetime.strptime(dataSet['received_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    if dataSet['supervisor_district'][i] not in delay_times:
        delay_times[dataSet['supervisor_district'][i]] = 0
    if dataSet['supervisor_district'][i] not in district_freq:
        district_freq[dataSet['supervisor_district'][i]] = 0
    delay_times[dataSet['supervisor_district'][i]] = delay_times[dataSet['supervisor_district'][i]] + dispatch.timestamp()-received.timestamp()
    district_freq[dataSet['supervisor_district'][i]] = district_freq[dataSet['supervisor_district'][i]] +1
    print(delay_times[dataSet['supervisor_district'][i]])

for key in delay_times:
    delay_times[key] = delay_times[key]/district_freq[key]

print(district_freq)
print(delay_times)