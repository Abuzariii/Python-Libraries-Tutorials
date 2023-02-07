#To create a profile report, copy the data file in a foder and open vs code there

import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv("gasprices.csv")
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="gasprices.html")