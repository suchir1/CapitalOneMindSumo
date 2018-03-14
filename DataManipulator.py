import pandas as pd
import os

@app.route('/')
cwd = os.getcwd()
print(cwd)
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_schema.csv")
print(dataSet)