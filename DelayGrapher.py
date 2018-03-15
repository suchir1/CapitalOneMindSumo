import plotly
from gmplot import gmplot
import os
import pandas as pd


cwd = os.getcwd()
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_data_subset.csv")
gmap = gmplot.GoogleMapPlotter(37.762289, -122.445359, 13)
gmap.heatmap(dataSet['latitude'], dataSet['longitude'])
gmap.draw("frequency.html")