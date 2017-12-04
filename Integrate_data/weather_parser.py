import numpy as np

if __name__ == "__main__":

	region = ["鞍部", "台北", "竹子湖", "社子", "大直", "石牌", "天母", "士林", "內湖", "南港", "大屯山", "信義", "文山"]

	for station in range(1,14):
		out = open('station'+str(station)+'.txt','w')
		out.write("name,date,time,temp,RH,WS,Precp\n")
		with open(region[station-1] + '_weather.txt') as f:
		    lines = f.readlines()
		    data = lines[0].split(',')
		    line=[]
		    for i in range(len(data)):
		    	
		    	if i % 8 == 0 and i != 0:
		    		out.write(",".join(line))
		    		out.write("\n")
		    		line=[]
		    	elif i % 8 == 7:
		    		continue
		    	line.append(data[i].strip(' \t\n\r  '))

		out.close()