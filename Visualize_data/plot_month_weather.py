import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time
from matplotlib.ticker import MaxNLocator
from pylab import figure, show, legend, ylabel
from scipy.stats import linregress

x=[]
y=[]
with open('bike_1.txt') as f:
    lines = f.readlines()
    lines = lines[1:]
    empty = [line.split(',')[2] for line in lines]
    x = [line.split(',')[5] for line in lines]
    inUse = [line.split(',')[6] for line in lines]
    day = [line.split(',')[10] for line in lines]
    time = [line.split(',')[11] for line in lines]
    weekday = [line.split(',')[12].strip() for line in lines]
    temp = [line.split(',')[-1] for line in lines]
    ws = [line.split(',')[-2] for line in lines]
    rh = [line.split(',')[-3] for line in lines]
    precp = [line.split(',')[-4] for line in lines]
# with open('station12.txt') as f:
#     lines = f.readlines()
#     lines = lines[1:]
#     temp = [line.split(',')[4] for line in lines]
#     date_temp = [line.split(',')[2] for line in lines]
    
# print(len(x))

date = [] #date
time_data = [] #time
inUse_data = [] #in_use
empty_data = []
temp_data = []
ws_data = []
rh_data = []
precp_data = []

count = 1 
inUse_count = 0
empty_count = 0


#得到指定日的資料
date = []
month = ['04', '05', '06', '07', '08']
for i in range(1, len(x)):
	if (day[i].split('-')[1] in month and day[i] not in time_data):
		time_data.append(day[i])	
	if (day[i].split('-')[1] in month and day[i].split('-')[2] == day[i-1].split('-')[2]): 
	# if (day[i].split('-')[1] in month and time[i].split(':')[0] == time[i-1].split(':')[0]): 
		inUse_count += (int)(inUse[i])
		empty_count += (int)(empty[i])
		count += 1	
	elif (day[i].split('-')[1] in month and day[i].split('-')[2] != day[i-1].split('-')[2]):
	# elif (day[i].split('-')[1] in month and time[i].split(':')[0] != time[i-1].split(':')[0]):
		
		if float(precp[i]) > 0:
			precp_data.append(float(precp[i]))
			inUse_data.append(inUse_count/count)
			empty_data.append(empty_count/count)
			temp_data.append(float(temp[i].strip("\n")))
			ws_data.append(float(ws[i]))
			rh_data.append(float(rh[i]))
			count = 1
			inUse_count = 0
			empty_count = 0
			date.append(day[i]+ time[i].split(':')[0])
	else:
		continue

# for i in range(len(date_temp)):
# 	if (date_temp[i].split('-')[1] == '5'):
# 		temp_data.append(temp[i])
# 	else:
# 		continue
# print (date)
# print (time_data) 
# print (len(time_data))
# print (len(inUse_data))
# print (len(temp_data))
# print (max(empty_data))
# print (min(empty_data))
# print (max(temp_data))
# print (min(temp_data))

# print (inUse_data)
# print (empty_data)
# print (temp_data)
# print (ws_data)
# print (rh_data)
# print (precp_data)

#得到指定星期的資料
#print (day)
'''month_data = np.arange(0,5)

quantity = np.zeros(5)


for i in range(len(x)):
	month = day[i].split('-')[1]
	
	if (month == '04'):
		month_data[0] += int(y[i])
		quantity[0] += 1
	elif (month == '05'):
		month_data[1] += int(y[i])
		quantity[1] += 1		
	elif (month == '06'):
		month_data[2] += int(y[i])
		quantity[2] += 1
	elif (month == '07'):
		month_data[3] += int(y[i])
		quantity[3] += 1
	elif (month == '08'):
		month_data[4] += int(y[i])
		quantity[4] += 1	
	else:
		continue

month_average = np.arange(0,5)

for i in range(0, 5):
	month_average[i] = month_data[i] / quantity[i]

'''




# ==================== plot both line for Temperature and Empty =======================

# # date = []
# # for j in range(1, len(x)):
# # 	if day[j].split('-')[1] in month:
# # 		if day[j] not in date:
# # 			date.append(day[j])

# data = [temp_data, ws_data, rh_data, precp_data]
# name = ["Temperature", "Wind Speed", "Relative Humidity", "Precipitation"]

# for index in range(len(data)):

# 	t = np.linspace(0, len(data[index]), num = len(month))
# 	w = ["2016-04", "2016-05", "2016-06", "2016-07", "2016-08"]

# 	fig1 = figure()
# 	ax1 = fig1.add_subplot(111)
# 	line1 = ax1.plot(range(len(data[index])), empty_data, label="Empty")
# 	ylabel("Number")
# 	# plt.xticks(t, w, rotation="vertical")
# 	plt.xticks(t, w)
# 	# now, the second axes that shares the x-axis with the ax1
# 	# ax2 = ax1.twinx()
# 	ax2 = fig1.add_subplot(111, frameon=False)
# 	line2 = ax2.plot(range(len(data[index])), data[index],'r', label=name[index]);  
# 	ax2.yaxis.tick_right()
# 	ax2.yaxis.set_label_position("right")
# 	ylabel(name[index])
# 	# plt.xticks(t, w, rotation="vertical")
# 	plt.xticks(t, w)

# 	# plt.xlabel('day')

# 	# plt.show()
# 	plt.savefig(name[index]+"_empty_daily_all_twoLine", dpi=600)

# ==================== plot both line for Temperature and Empty =======================


# ==================== plot correlation for Attribute and In use =======================

# # data = [temp_data, ws_data, rh_data, precp_data]
# # name = ["Temperature", "Wind Speed", "Relative Humidity", "Precipitation"]

# # for item in data:

# slope, intercept, r, p, std = linregress(inUse_data, precp_data)

# x = np.array(range(len(inUse_data)))
# y = slope*x + intercept

# plt.scatter(inUse_data, precp_data, s = 3)
# plt.plot(x, y, 'r', label="Precipitation")  
# plt.title('Scatter')
# plt.xlabel('In use')
# plt.ylabel('Precipitation')
# plt.legend()
# plt.grid(True)
# plt.show()

# ==================== plot correlation for Attribute and In use =======================

# ==================== plot correlation for Attribute and Empty =======================

data = [temp_data, ws_data, rh_data, precp_data]
# data = [rh_data]

name = ["Temperature", "Wind Speed", "Relative Humidity", "Precipitation"]

# name = ["Relative Humidity"]

for index in range(len(data)):
	# for n in range(3,7):
	# 	z = np.polyfit(empty_data, data[index], n)
	# 	p = np.poly1d(z)
	# 	x = np.array(range(round(max(empty_data))))
	# 	y = p(x)

	slope, intercept, r, p, std = linregress(empty_data, data[index])

	x = np.array(range(round(max(empty_data))))
	y = slope*x + intercept
	plt.figure()
	plt.scatter(empty_data, data[index], s = 3)
	plt.plot(x, y, 'r', label=name[index])  
	plt.title('Scatter')
	plt.xlabel('Empty')
	plt.ylabel(name[index])
	plt.legend()
	plt.grid(True)
	# plt.show()
	plt.savefig(name[index]+"_empty_hourly_all_linear_withRain", dpi=600)

		# plt.savefig(name[index]+"_empty_daily_all_linear", dpi=600)
		# print(np.corrcoef(empty_data, precp_data))


# ==================== plot correlation for Attribute and Empty =======================


