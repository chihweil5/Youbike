import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time
from matplotlib.ticker import MaxNLocator
from pylab import figure, show, legend, ylabel
from scipy.stats import linregress
from scipy.stats import scoreatpercentile
import statsmodels.api as sm
import pandas as pd
import sklearn.cross_validation
from sklearn.cross_validation import train_test_split
from sklearn import linear_model

x=[]
y=[]

work_area = ",".join(open('work_area.txt').readlines()).replace("\n", "").split(",")
school_area = ",".join(open('school_area.txt').readlines()).replace("\n", "").split(",")
hotSpot_area = ",".join(open('hotspot_area.txt').readlines()).replace("\n", "").split(",")
residental_area = ",".join(open('house_area.txt').readlines()).replace("\n", "").split(",")
# work_area = [1]

frames = []
for spot in residental_area:
    bike = pd.read_csv('bike_weather_data/bike_'+str(spot)+'.txt')
    # bike = pd.read_csv('bike_weather_data/bike_1.txt')
    frames.append(bike)
result = pd.concat(frames)


empty = result['empty'].tolist()
x = result['time'].tolist()
inUse = result['in_use'].tolist()
total = result['total'].tolist()
day = result['date'].tolist()
time = result['timestamp'].tolist()
weekday = result['week'].tolist()
temp = result['temp'].fillna(0).tolist()
ws = result['WS'].fillna(0).tolist()
rh = result['RH'].fillna(0).tolist()
precp = result['Precp'].fillna(0).tolist()  

date = [] #date
time_data = [] #time
inUse_data = [] #in_use
empty_data = []
temp_data = []
ws_data = []
rh_data = []
precp_data = []
hour_data = []
week_data = []

count = 1 
inUse_count = 0
empty_count = 0


date = []
month = ['04', '05', '06', '07', '08']
for i in range(1, len(x)):
    if day[i].split('-')[1] in month and day[i] not in time_data:
        time_data.append(day[i])
    # if (day[i].split('-')[1] in month and day[i].split('-')[2] == day[i-1].split('-')[2]): 
    # if (day[i].split('-')[1] in month and time[i].split(':')[2] == time[i-1].split(':')[2]):
    if day[i].split('-')[1] in month and time[i].split(':')[0] == '01':
    # if day[i].split('-')[1] in month and weekday[i] == 1:
        inUse_count += (int)(inUse[i])
        empty_count += (int)(empty[i])
        count += 1
    elif day[i].split('-')[1] in month and time[i-1].split(':')[0] == '01':
        # print(day[i].split('-')[1])
    # elif day[i].split('-')[1] in month and weekday[i-1] == 1:
        inUse_data.append(inUse_count/count/total[i]*100)
        empty_data.append(empty_count/count/total[i]*100)
        week_data.append(float(weekday[i]))
        hour_data.append(float(time[i].split(':')[0]))
        temp_data.append(float(temp[i]))
        ws_data.append(float(ws[i]))
        rh_data.append(float(rh[i]))
        precp_data.append(float(precp[i]))
        count = 1
        inUse_count = 0
        empty_count = 0
        date.append(day[i]+ time[i].split(':')[0])
    else:
        continue
    

X = np.column_stack((hour_data, temp_data, ws_data, precp_data, rh_data))
# X = np.column_stack((hour_data, temp_data))
X = sm.add_constant(X)#add intercept
y = empty_data
# print(len(X))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(len(X_test))
print(len(X_train))

lr = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
model = lr.fit(X_train, y_train)
predictions = model.predict(X_test)
# input()
# print(len(y))
#predict y= c1*x1+ c2*x2+c3*x3+c4* x4 + b

# model = sm.OLS( y_train, X_train ).fit()
# print(model.summary())
# predictions = model.predict(X_test)
count = 0
for index in range(len(y_test)):
    # print(y_test[index], predictions[index])
    # input()
    if abs(int(y_test[index]) - int(abs(predictions[index]))) < 15:
        count += 1

print("Accuracy: %f" %(count/len(X_test)))
plt.scatter(abs(predictions), y_test, s=3)
plt.xlabel("Predicted Values from model")
plt.ylabel("Actual Values empty_data")
# plt.show()
#=====================

