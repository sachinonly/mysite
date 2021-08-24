import pandas
from pytz import utc
from datetime import datetime
import matplotlib.pyplot as plt
data =  pandas.read_csv("C:\\Users\\sachin-windows\\Heloworld\\files\\reviews.csv", parse_dates=['Timestamp'])
data[( data["Rating"]>4)   &  (data["Course Name"] == 'The Python Mega Course: Build 10 Real World Applications')  ] ['Rating']
data[data['Comment'].notnull()]
data[data["Comment"].str.contains('accent', na=False)]["Rating"]
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()
day_average
plt.plot(day_average.index,day_average['Rating'])

# For month

# import pandas
# from pytz import utc
# from datetime import datetime
# import matplotlib.pyplot as plt
# data =  pandas.read_csv("C:\\Users\\sachin-windows\\Heloworld\\files\\reviews.csv", parse_dates=['Timestamp'])
# data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
# month_average = data.groupby(['Month']).mean()
# month_average
# plt.plot(month_average.index,month_average['Rating'])