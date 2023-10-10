import pandas as pd

data = pd.read_csv("./day-25/2018_Central_Park_Squirrel_Census.csv")

fur_summary = data.value_counts("Primary Fur Color").to_frame(name="count")
print(fur_summary)
fur_summary.to_csv("./day-25/squirrel_count.csv")
