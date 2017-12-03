import numpy as np
import pandas as pd
import datetime


if __name__ == "__main__":
    
    bike = pd.read_csv("./bike_output.txt")
    
    #split date and time
    date = pd.DataFrame(bike.time.str.split(' ',1).tolist(),
                                   columns = ['date','timestamp'])
    bike = pd.concat([bike, date], axis=1)

    #add weekday/weekend
    weekRow = []
    for index,row in bike.iterrows():
        date = datetime.datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S')
        weekRow.append(date.weekday())
        #bike.loc[index,'week'] = date.weekday()

    bike['week'] = pd.Series(np.array(weekRow), index=bike.index)

    #bike.to_csv("./bike_output.txt")
    
    
    for i in range(1,393):
        file = str(i) + '.txt'
        bike[bike.id == i].to_csv(file, index=False)
    

