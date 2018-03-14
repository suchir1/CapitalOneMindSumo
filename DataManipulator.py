import pandas as pd
import os

cwd = os.getcwd()
print(cwd)
dataSet = pd.read_csv(cwd + "/Data/sfpd_dispatch_schema.csv")
print(dataSet)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)