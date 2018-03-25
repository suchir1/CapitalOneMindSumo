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
    if not pd.notnull(dataSet['call_type'][i]) or not pd.notnull(dataSet['supervisor_district'][i]):
        continue
    if dataSet['supervisor_district'][i] == 7:
        if dataSet['call_type'][i] not in delay_times:
            delay_times[dataSet['call_type'][i]] = 0
        delay_times[dataSet['call_type'][i]] = delay_times[dataSet['call_type'][i]] +1

print(delay_times)