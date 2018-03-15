import plotly
from gmplot import gmplot
import os
import pandas as pd


cwd = os.getcwd()
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_data_subset.csv")
gmapFrequency = gmplot.GoogleMapPlotter(37.762289, -122.445359, 13)
gmapFrequency.heatmap(dataSet['latitude'], dataSet['longitude'])
gmapFrequency.draw("frequency.html")

gmapNotUrgent = gmplot.GoogleMapPlotter(37.762289, -122.445359, 13)
gmapUrgent = gmplot.GoogleMapPlotter(37.762289, -122.445359, 13)
notUrgentCoords = list()
urgentCoords = list()
for i in range(len(dataSet['received_timestamp'])):
    if dataSet['final_priority'][i]==2:
        notUrgentCoords.append((dataSet['latitude'][i], dataSet['longitude'][i]))
    elif dataSet['final_priority'][i]==3:
        urgentCoords.append((dataSet['latitude'][i], dataSet['longitude'][i]))

#Gets the latitudes and longitudes into separate lists instead of in tuples
notUrgentlats, notUrgentlongs = zip(*notUrgentCoords)
urgentLats, urgentLongs = zip(*urgentCoords)

gmapNotUrgent.heatmap(notUrgentlats, notUrgentlongs)
gmapNotUrgent.draw("notUrgent.html")
gmapUrgent.heatmap(urgentLats,urgentLongs)
gmapUrgent.draw("urgent.html")