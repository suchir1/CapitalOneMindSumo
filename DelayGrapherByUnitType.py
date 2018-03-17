import pandas as pd
import os
import datetime
import plotly
import plotly.graph_objs as go

cwd = os.getcwd()
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_data_subset.csv")

#delay_times contains the month and year as the key and the delay as the value
#district_freq contains the month and year as the key and the number of times that supervisor district is called as the value
delay_times = {}
district_freq = {}

for i in range(len(dataSet['on_scene_timestamp'])):
    if not pd.notnull(dataSet['on_scene_timestamp'][i]) or not pd.notnull(dataSet['supervisor_district'][i]):
        continue
    on_scene = datetime.datetime.strptime(dataSet['on_scene_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    received = datetime.datetime.strptime(dataSet['received_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    if dataSet['unit_type'][i] not in delay_times:
        delay_times[dataSet['unit_type'][i]] = 0
    if dataSet['unit_type'][i] not in district_freq:
        district_freq[dataSet['unit_type'][i]] = 0
    delay_times[dataSet['unit_type'][i]] = delay_times[dataSet['unit_type'][i]] + on_scene.timestamp()-received.timestamp()
    district_freq[dataSet['unit_type'][i]] = district_freq[dataSet['unit_type'][i]] +1

x = list()
y = list()
for key in delay_times:
    delay_times[key] = delay_times[key]/district_freq[key]
    x.append(key)
    y.append(delay_times[key])


print(delay_times)



trace = go.Bar(x = x, y=y)

data = [trace]

plotly.offline.plot(data, filename='OnSceneDelayByUnitType.html')

