# import time
# import os
# import pandas
#
# while True:
#     if os.path.exists("files/temps_today.csv"):
#         data=pandas.read_csv("files/temps_today.csv")
#         print (data.mean())
#     else:
#         print("File does not exist")
#     time.sleep(3)

#df1=pandas.DataFrame([[1,2,3],[9,8,6],[5,6,7]], columns=["col1","col2","col3"])
#df1=pandas.DataFrame([[1,2,3],[9,8,6],[5,6,7]], columns=["col1","col2","col3"], index=["Row1","Row2","Row3"])
#df2=pandas.DataFrame([{"Key1":"value1"},{"Key2":"value2"},{"key3":"value3"},{"Key1":"Value4"},{"Key1":"Value5"},{"Key1":"Value6"}])


import os
import pandas
df1=pandas.read_csv("C:\\Personals\\Learnings\\Python\\supermarkets\\supermarkets.csv")
df1
import sys

locate_python = sys.exec_prefix
print(locate_python)