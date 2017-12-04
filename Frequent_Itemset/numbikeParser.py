import numpy as np
import pandas as pd
import datetime

if __name__ == "__main__":
    
    bike = pd.read_csv("./bike_output.txt")
    
    fileout = open('frequentItemSet_time.txt','w')
    fileout.write("ID,Name,Time,Quantity\n")

    #bikeFilter = pd.DataFrame(bike[bike['in_use'] <= 5]['week'])
    
    for index, item in bike[bike['in_use'] == 0].iterrows():
    	# get data in a month
        # month = item['date'].split("-")[1]
        # if(month == '05'):
    	# 	fileout.write(str(item['id'])+','+item['name']+','+item['timestamp'].split(":")[0]+',1\n')
        fileout.write(str(item['id'])+','+item['name']+','+'week_'+str(item['week']+1)+'-'+item['timestamp'].split(":")[0]+',1\n')
        fileout.write(str(item['id'])+','+item['name']+','+item['timestamp'].split(":")[0]+',1\n')
    

