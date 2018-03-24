import pandas as pd
import os
import datetime
import plotly
import plotly.graph_objs as go

cwd = os.getcwd()
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_data_subset.csv")


#The keys for this dictionary are the obfuscated address combined with the hour of the day and the values begin as a dictionary of how many times each unit gets called
# and after processing becomes just the name of the unit that gets called the most.
dispatchDict = {}
district_freq = {}

for i in range(len(dataSet['received_timestamp'])):
    if not pd.notnull(dataSet['address'][i]) or not pd.notnull(dataSet['received_timestamp'][i]):
        continue
    received = datetime.datetime.strptime(dataSet['received_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    hour = received.hour
    hour = str(hour)
    if len(hour)==1:
        hour = "0"+hour
    key = dataSet['address'][i]+" " + hour
    key = key.lower()
    if key not in dispatchDict:
        dispatchDict[key] = {}
    unitType = dataSet['unit_type'][i]
    if unitType not in dispatchDict[key]:
        dispatchDict[key][unitType] = 0
    dispatchDict[key][unitType] = dispatchDict[key][unitType] + 1

for key in dispatchDict:
    max = -1
    maxUnit = ""
    for unit in dispatchDict[key]:
        if dispatchDict[key][unit] > max:
            max = dispatchDict[key][unit]
            maxUnit = unit
    dispatchDict[key] = maxUnit

print(dispatchDict)