import numpy as np
import pandas as pd

csv_name_set = set()
while True:
   i = input("enter csv name to add to merger, or press enter to merge ")
   if i == "":
       break
   else :
       csv_name_set.add(i)

df_list = []
for i in csv_name_set:
    df_list.append(pd.read_csv("./raw_data/" + i, 
                               usecols=["Name", "Date", "Last price"],
                               parse_dates = ["Date"]
                               ))
df_merged = pd.concat(df_list, axis=0).set_index(["Name", "Date"])

print (df_merged)
 
#df_merged.to_csv("merged.csv")











