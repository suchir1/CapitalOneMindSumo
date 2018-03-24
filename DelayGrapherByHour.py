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

for i in range(len(dataSet['dispatch_timestamp'])):
    if not pd.notnull(dataSet['dispatch_timestamp'][i]) or not pd.notnull(dataSet['supervisor_district'][i]):
        continue
    dispatch = datetime.datetime.strptime(dataSet['dispatch_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    received = datetime.datetime.strptime(dataSet['received_timestamp'][i], "%Y-%m-%d %H:%M:%S.%f %Z")
    if dataSet['received_timestamp'][i][11:13] not in delay_times:
        delay_times[dataSet['received_timestamp'][i][11:13]] = 0
    if dataSet['received_timestamp'][i][11:13] not in district_freq:
        district_freq[dataSet['received_timestamp'][i][11:13]] = 0
    delay_times[dataSet['received_timestamp'][i][11:13]] = delay_times[dataSet['received_timestamp'][i][11:13]] + dispatch.timestamp()-received.timestamp()
    district_freq[dataSet['received_timestamp'][i][11:13]] = district_freq[dataSet['received_timestamp'][i][11:13]] +1

x = list()
y = list()
for key in delay_times:
    delay_times[key] = delay_times[key]/district_freq[key]
    x.append(key)

x.sort()

for key in x:
    y.append(delay_times[key])

print(delay_times)

trace = go.Scatter(x = x, y=y)

layout = go.Layout(
    title='On-Scene Delay by Hour',
    font=dict(family='Courier New, monospace', size=16, color='#1E8449'),
    xaxis=dict(
        title='Hour',
        titlefont=dict(
            family='Courier New, monospace',
            size=14,
            color='#7D3C98'
        )
    ),
    yaxis=dict(
        title='Average Delay to get On the Scene (seconds)',
        range=[0, 1100],
        titlefont=dict(
            family='Courier New, monospace',
            size=14,
            color='#7D3C98'
        )
    )
)



data = [trace]
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='On-Scene Delay by Hour.html')

