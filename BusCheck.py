#Importing things
import snscrape.modules.twitter as sntwitter
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Creating list to append tweet data to
tweets_list1 = []
date=[]
content=[]
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:dublinbusnews').get_items()):
#i references the tweet
    if i>700:
        break
    tweets_list1.append([tweet.date, tweet.content])
    date.append(tweet.date)
    content.append(tweet.content)
# Creating a dataframe from the tweets list above
#In hindsight, pd.dataframe has a date handler so I could have used that instead of datetime but I've not used pands much
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Text'])

curtCon=[]
curtDate=[]
#Looking for Diversion and Curtailment as keywords in the tweet
for i in range(0, len(content)):
    if ("Curtailment" in content[i] or "Diversion" in content[i]):
        curtCon.append(content[i])
        curtDate.append(date[i])

pltD=[]
pltT=[]
#Spliting the datetime into Hour.Minute and Day Month Year then storing day in its own away
for i in range(0,len(curtDate)):
    pltT.append(float(curtDate[i].strftime("%H.%M")))
    pltD.append(curtDate[i].strftime("%d-%m-%Y"))

day=[]

for i in range(0,len(pltD)):
    day.append(datetime.datetime.strptime(pltD[i], '%d-%m-%Y'))

dayno=[]
#Convterting date to day. I didnt check if this was right, but let's assume it is
#strftime("%A") converts it from a number to the name of the day
for i in range(0,len(pltD)):
    dayno.append(day[i].weekday())
    day[i]=day[i].strftime("%A")
angelus=[]
ang2=[]
ang3=[]
#The angelus is a mathematical constant - I'm surprised it's not part of the numpy library
for i in range(0,len(pltT)):
    angelus.append(6.00)
    ang2.append(12.00)
    ang3.append(18.00)
#I hard the Corrie time - I dont have an API for the Virgin Media daily calenday
corrie = [20.00, 19.30,0,0,20.00,0,0,19.30,0,0,0,0,20.00,0,0,0,20.00,19.30,19.30,0,0,0,0]
corrie2= [20.30,20.30,0,0,20.30,0,0,20.30,0,0,0,0,20.30,0,0,0,20.30,20.30,20.30,0,0,0,0]

#I started trying to fit a line to the day, but that's a work in progress
dayfit=[4, 2, 1, 1, 4, 3, 6, 0, 6, 6, 5, 5, 4, 3, 3, 3]


#Plotting
plt.plot_date(day,pltT,label="Tweet announcing curtailment on Dublin Bus routes")
plt.plot_date(day,ang2,label="Angelus",linestyle='-',marker=" ",color="g")
plt.plot_date(day,ang3,linestyle='-',marker=" ",color="g")
plt.plot_date(day,corrie,label="Coronation Street airing on Virgin Media 1" , linestyle=' ',marker="*",color="r")
plt.plot_date(day,corrie2,linestyle=' ',marker="*",color="r")
plt.ylim(6,22)
plt.xlabel("Day")
plt.title("Dublin Bus Route Curtailment")
plt.ylabel("Time")
plt.legend()
plt.show()
