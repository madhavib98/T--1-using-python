import json
import matplotlib.pyplot as plt
from datetime import datetime as d

with open('data.json') as f:
    data=json.load(f)
first=d(2019,1,1)
last=d(2019,1,31)
date=[]
value=[]
for i in data['rates']:
    day = d.strptime(i,'%Y-%m-%d')
    if day >= first and day <= last:
      date.append(i)
      value.append(data['rates'][i]['INR'])



plt.plot(date,value,'go--', linewidth=1, linestyle='solid',color='blue')
plt.xlabel('Dates')
plt.xticks(rotation=90)
plt.ylabel('Values')
plt.title('INR exchange rate against EUR')
plt.show() 