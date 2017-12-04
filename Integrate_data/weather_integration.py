import numpy as np
import pandas as pd
import datetime

def add_weather(weather, bike):
    temp=[]
    RH=[]
    WS=[]
    Precp=[]
    weatherRow = 12
    bikeRow = 0

    bikeSize = bike['date'].count()
    weatherSize = weather['time'].count()
    print(weatherSize)

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

def output_file(bike_weather):
    bike_weather.to_csv("test.txt", index=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Data Mining HW2')
    parser.add_argument('-b', type=str,
                            help="Input the bike station", 
                            required=True)
    parser.add_argument("-w", type=str, 
                            help="Input the weather station corresponded to the bike station", 
                            required=True)
   

    args = parser.parse_args()

    weather = pd.read_csv('station12.txt')
    bike = pd.read_csv("1.txt")

    bike_weather = add_weather(weather, bike)
    output_file(bike_weather)
            


