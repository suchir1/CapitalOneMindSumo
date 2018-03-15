import pandas as pd
import os
import datetime
import numpy as np

#Calculates the time between the emergency call being received
#and the unit reaching the location of the incident

cwd = os.getcwd()
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_data_subset.csv")
dataSet['delay_time'] = dataSet['latitude'].copy()
for i in range(len(dataSet['received_timestamp'])):
    if not pd.notnull(dataSet['on_scene_timestamp'][i]):
        dataSet['delay_time'][i] = np.NaN
        continue
    onscene = datetime.datetime.strptime(dataSet['on_scene_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    received = datetime.datetime.strptime(dataSet['received_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    dataSet['delay_time'][i] = onscene.timestamp()-received.timestamp()
pd.DataFrame.to_clipboard(dataSet)
