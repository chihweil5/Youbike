import numpy as np
import pandas as pd
import datetime
import argparse
import math

def add_weather(weather, bike):
    temp=[]
    RH=[]
    WS=[]
    Precp=[]
    weatherRow = 12
    bikeRow = 0

    bikeSize = bike['date'].count()
    weatherSize = weather['time'].count()
    print("Weather data size: ", weatherSize)

    while bikeRow < bikeSize and weatherRow < weatherSize:
        date = datetime.datetime.strptime(bike['date'][bikeRow], '%Y-%m-%d')
        time = bike['timestamp'][bikeRow].split(':')
        weatherTime = weather['time'][weatherRow].split(':')
        weatherDate = datetime.datetime.strptime(weather['date'][weatherRow], '%Y-%m-%d')
        if weatherTime[0] == '24':
            weatherTime[0]='0'
            weatherDate += datetime.timedelta(days=1)
        
        if date == weatherDate and int(time[0]) == int(weatherTime[0]):
            temp.append(weather['temp'][weatherRow])
            RH.append(weather['RH'][weatherRow])
            WS.append(weather['WS'][weatherRow])
            Precp.append(weather['Precp'][weatherRow])
            # print(bike['date'][bikeRow], bike['timestamp'][bikeRow])
            # print(weather['date'][weatherRow], weather['time'][weatherRow])
            bikeRow += 1
        else:
            weatherRow += 1
        
    w = pd.DataFrame({'temp': temp, 'RH':RH, 'WS':WS, 'Precp':Precp})
    bike = bike.join(w)
    return bike

def output_file(bike_weather, filename):
    bike_weather.to_csv("./bike_weather_data/"+filename, index=False)

def calculate_distance(lon, lat):
    station_loc = ([(121.529731, 25.182586), (121.514853, 25.037658), (121.544547, 25.162078), (121.469681, 25.109508), 
    (121.542853, 25.078047), (121.513817, 25.116342), (121.537169, 25.117494), (121.503019, 25.090253), (121.575450, 25.079422), 
    (121.602906, 25.055431), (121.522408, 25.175675), (121.564597, 25.037822), (121.575728, 25.002350)])
    min_dis = float('inf')
    min_dis_index = 0
    i = 0
    for loc in station_loc:
        i += 1
        dis = math.sqrt( (lon - loc[0])**2 + (lat - loc[1])**2 )
        if min_dis > dis:
            min_dis = dis
            min_dis_index = i
    
    if min_dis_index > 13 or min_dis_index == 0:
        print("Error station file")
    return min_dis_index


if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='Integrate weather data to station data')
    # parser.add_argument('-b', type=str,
    #                         help="Input the bike station", 
    #                         required=True)
    # parser.add_argument("-w", type=str, 
    #                         help="Input the weather station corresponded to the bike station", 
    #                         required=True)
    # parser.add_argument("-o", type=str, 
    #                         help="Output file name", 
    #                         required=True)
   

    # args = parser.parse_args()
    # weather = pd.read_csv(args.w)
    # bike = pd.read_csv(args.b)
    # out = args.o + ".txt"

    # bike_weather = add_weather(weather, bike)
    # output_file(bike_weather, out)

    # Integrate weather to all bike stations
    for i in range(1,393):
        bike = pd.read_csv(str(i) + ".txt")
        if bike.empty:
            continue
        lon = bike['lng'][0]
        lat = bike['lat'][0]
        weather_file = calculate_distance(lon, lat)
        weather = pd.read_csv("./weather/station" + str(weather_file) + ".txt")
        out = "bike_" + str(i) + ".txt"
        bike_weather = add_weather(weather, bike)
        #output_file(bike_weather, out)
        print("Combine bike" + str(i) + " with weather station" + str(weather_file))



    
            


