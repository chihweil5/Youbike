import numpy as np
import pandas as pd
import datetime
from datetime import time
import collections
import matplotlib.pyplot as plt


def plotWeek(bike):
    weekX =[]
    weekY =[]

    for i in range(7):
        week = bike.loc[lambda df: bike.week == i]

        timeDict={}

        for index, row in week.iterrows():
            timestamp = row['timestamp'].split(':')
            time = int(str(timestamp[0]) + str(timestamp[1]))
            if time not in timeDict:
                timeDict[time] = (int(row['empty']), 1)
            else:
                timeDict[time] = (timeDict[time][0] + int(row['empty']), timeDict[time][1]+1)
        
        ordered = collections.OrderedDict(sorted(timeDict.items()))

        x=[]
        y=[]
        
        for k, v in ordered.items(): 
            x.append(k)
            y.append(v[0]/v[1])

        weekX.append(x)
        weekY.append(y)
    
    week_name=['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    color=['orange','green', 'blue', 'tan', 'red', 'purple', 'pink']
    
    
    for i in range(7):
        plt.figure()
        plt.xlabel("Time")
        plt.ylabel("Empty")
        plt.title(week_name[i])
        xTicks = np.linspace(0, 24, num=len(weekX[i]))
        plt.scatter(xTicks, weekY[i], color=color[i], label=week_name[i])
        t=np.arange(24)
        plt.xticks(range(24), (t))
        
        plt.legend(loc='lower right')
        plt.savefig(week_name[i]+'.png', dpi = 600)

def getWeekday(bike):
    week = bike.loc[lambda df: bike.week < 5]

    timeDict={}

    for index, row in week.iterrows():
        timestamp = row['timestamp'].split(':')
        time = int(str(timestamp[0]) + str(timestamp[1]))
        if time not in timeDict:
            timeDict[time] = (int(row['empty']), 1)
        else:
            timeDict[time] = (timeDict[time][0] + int(row['empty']), timeDict[time][1]+1)
    
    ordered = collections.OrderedDict(sorted(timeDict.items()))

    x=[]
    y=[]
    
    for k, v in ordered.items(): 
        x.append(k)
        y.append(v[0]/v[1])

    return x, y

def getWeekend(bike):

    week = bike.loc[lambda df: bike.week >= 5]

    timeDict={}

    for index, row in week.iterrows():
        timestamp = row['timestamp'].split(':')
        time = int(str(timestamp[0]) + str(timestamp[1]))
        if time not in timeDict:
            timeDict[time] = (int(row['empty']), 1)
        else:
            timeDict[time] = (timeDict[time][0] + int(row['empty']), timeDict[time][1]+1)
    
    ordered = collections.OrderedDict(sorted(timeDict.items()))

    x=[]
    y=[]
    
    for k, v in ordered.items(): 
        x.append(k)
        y.append(v[0]/v[1])

    return x, y


if __name__ == "__main__":

    bike = pd.read_csv("97.txt")

    
    # Week
    # plotWeek(bike)

    # Weekend/Weekdat
    x1, y1 = getWeekend(bike)
    x2, y2 = getWeekday(bike)

    plt.xlabel("Time")
    plt.ylabel("Empty")

    xTicks1 = np.linspace(0, 24, num=len(x1))
    plt.scatter(xTicks1, y1, color='blue', s=5, label='weekend', linewidth=0.3)

    xTicks2 = np.linspace(0, 24, num=len(x2))
    plt.scatter(xTicks2, y2, color='red', s=5, label='weekday', linewidth=0.3)

    t=np.arange(24)
    plt.xticks(range(24), (t))

    plt.legend(loc='lower right')
    plt.savefig('week_empty_捷運劍潭站(2號出口).jpg', dpi = 600)
    plt.show()



    
