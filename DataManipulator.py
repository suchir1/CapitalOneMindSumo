import pandas as pd
import os

cwd = os.getcwd()
print(cwd)
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_schema.csv")
pd.DataFrame.to_clipboard(dataSet)