import coinmarketcap
import pandas as pd
import time
import datetime

#Grabs coins and basic data from coinmarketcap and places it in a csv called top coins

market = coinmarketcap.Market()
coins = market.ticker()

for i in range(96):
    #this creates a dataframe with the top 100 coins
    coinArray = pd.DataFrame([pd.Series(coins[i]) for i in range(100)]).set_index('id')

    #timestamps and stores the csv file
    location = 'Data/'+str(time.time())+'.csv'
    csvFile = '{}coins.csv'.format(datetime.date.today())
    #This is only used for the general day if you want to add minutes to the name of the csvfile uncomment the following lines:
    #now = datetime.datetime.now()
    #csvFile = '{}coins.csv'.format(now.strftime("%Y-%m-%d_%H-%M")) #not using seconds because it splits into seperate files and I do not need it to be that accurate
    coinArray.to_csv(csvFile)


