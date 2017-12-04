#Fall 2017, CSCI 4502/5502: Data Mining 
#Final Project - Fetch weather data
#Dataset: http://e-service.cwb.gov.tw/HistoryDataQuery/

import urllib.request
import time
from lxml import etree

if __name__ == "__main__":
	# tStart = time.time()
	region = ["鞍部", "台北", "竹子湖", "社子", "大直", "石牌", "天母", "士林", "內湖", "南港", "大屯山", "信義", "文山"]
	output = []

	month_list = ['04', '05', '06', '07', '08']
	date_list = []
	# fileout = open(region[3]+'_weather.txt','w')
	fileout = open("文山"+'_weather.txt','w')
	for month in range(4, 9):
		# 鞍部
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466910&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker=2016-"+str(month)+"-"+str(date)
		# 台北
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker=2016-"+str(month)+"-"+str(date)
		# 竹子湖
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466930&stname=%25E7%25AB%25B9%25E5%25AD%2590%25E6%25B9%2596&datepicker=2016-"+str(month)+"-"+str(date)
		# 社子
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0A980&stname=%25E7%25A4%25BE%25E5%25AD%2590&datepicker=2016-"+str(month)+"-"+str(date)
		# 大直
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0A9A0&stname=%25E5%25A4%25A7%25E7%259B%25B4&datepicker=2016-"+str(month)+"-"+str(date)
		# 石牌
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0A9B0&stname=%25E7%259F%25B3%25E7%2589%258C&datepicker=2016-"+str(month)+"-"+str(date)
		# 天母
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0A9C0&stname=%25E5%25A4%25A9%25E6%25AF%258D&datepicker=2016-"+str(month)+"-"+str(date)
		# 士林
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0A9E0&stname=%25E5%25A3%25AB%25E6%259E%2597&datepicker=2016-"+str(month)+"-"+str(date)
		# 內湖
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0A9F0&stname=%25E5%2585%25A7%25E6%25B9%2596&datepicker=2016-"+str(month)+"-"+str(date)
		# 南港
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0A9G0&stname=%25E5%258D%2597%25E6%25B8%25AF&datepicker=2016-"+str(month)+"-"+str(date)
		# 大屯山
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0AC40&stname=%25E5%25A4%25A7%25E5%25B1%25AF%25E5%25B1%25B1&datepicker=2016-"+str(month)+"-"+str(date)
		# 信義
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0AC70&stname=%25E4%25BF%25A1%25E7%25BE%25A9&datepicker=2016-"+str(month)+"-"+str(date)
		# 文山
		# url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0AC80&stname=%25E6%2596%2587%25E5%25B1%25B1&datepicker=2016-"+str(month)+"-"+str(date)
		


		if month != 4 and month != 6:
			for date in range(1, 32):
				url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0AC80&stname=%25E6%2596%2587%25E5%25B1%25B1&datepicker=2016-"+str(month)+"-"+str(date)
				response = urllib.request.urlopen(url)
				html = response.read()

				time = []
				page = etree.HTML(html)
				# print(page.xpath(u"//tr[3]/td/text()"))

				tr_list = [1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

				use_list = [0, 3, 5, 6, 10, 13]

				data = page.xpath(u"//tr[1]/td/text()")
				for i in data:
					time.append(i.split(':')[1].strip(' '))

				for i in range(3, 27):
					data = page.xpath(u"//tr["+str(i)+"]/td/text()")
					td_count = 0
					output.append(time[0])
					output.append(time[1])
					for j in data:
						if td_count in use_list:
							if td_count == 0:
								output.append(j.strip('\xa0')+':00')
							else:
								output.append(j.strip('\xa0'))
						td_count += 1
		else:	
			for date in range(1, 31):
				url = "http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0AC80&stname=%25E6%2596%2587%25E5%25B1%25B1&datepicker=2016-"+str(month)+"-"+str(date)
				response = urllib.request.urlopen(url)
				html = response.read()

				time = []
				page = etree.HTML(html)
				# print(page.xpath(u"//tr[3]/td/text()"))

				tr_list = [1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

				use_list = [0, 3, 5, 6, 10, 13]

				data = page.xpath(u"//tr[1]/td/text()")
				for i in data:
					time.append(i.split(':')[1].strip(' '))

				for i in range(3, 27):
					data = page.xpath(u"//tr["+str(i)+"]/td/text()")
					td_count = 0
					output.append(time[0])
					output.append(time[1])
					for j in data:
						if td_count in use_list:
							if td_count == 0:
								output.append(j.strip('\xa0')+':00')
							else:
								output.append(j.strip('\xa0'))
						td_count += 1

	fileout.write(", ".join(output))
	fileout.close()
	# tEnd = time.time()
	# print("It cost %f sec" % (tEnd - tStart))
