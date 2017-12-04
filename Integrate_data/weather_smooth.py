import numpy as np
import pandas as pd

if __name__ == "__main__":

	for station in range(1,14):
		
		weather = pd.read_csv('station'+str(station)+'.txt')

		#print(weather)

		weather[['temp', 'RH', 'WS', 'Precp']] = weather[['temp', 'RH', 'WS', 'Precp']].apply(pd.to_numeric, errors='coerce')
		
		#print(weather['Precp'][230:240])

		for i in range(0, len(weather.index), 24):

			temp_ave = weather['temp'][i:i+24].mean()
			RH_ave = weather['RH'][i:i+24].mean()
			WS_ave = weather['WS'][i:i+24].mean()
			Precp_ave = weather['Precp'][i:i+24].mean()

			weather.loc[i:i+24, 'temp'].fillna(temp_ave, inplace=True)
			weather.loc[i:i+24, 'RH'].fillna(RH_ave, inplace=True)
			weather.loc[i:i+24,'WS'].fillna(WS_ave, inplace=True)
			weather.loc[i:i+24, 'Precp'].fillna(Precp_ave, inplace=True)
		
		#out = open('station'+str(station)+'.txt','w')
		weather.to_csv('station'+str(station)+'.txt', index=False)