from matplotlib import pyplot as  plt
import pandas as pd
import numpy as np

fifa = pd.read_csv("E:\Pyhton\Matplotlib\Fifa.csv")

plt.title("Players Distribution by Wages in FIFA 18", fontdict={'fontsize': 20})

fifa.Wage = [ x.strip('K') if type(x)==str else x for x in fifa.Wage]
fifa.Wage = [ x.strip('€') if type(x)==str else x for x in fifa.Wage]
fifa['Wage'] = fifa.Wage.astype(int)


very_high = fifa.loc[fifa.Wage>300].count()[0]
high = fifa.loc[(fifa.Wage>250) & (fifa.Wage<300)].count()[0]
medium = fifa.loc[(fifa.Wage>200) & (fifa.Wage < 250)].count()[0]
low = fifa.loc[(fifa.Wage>160) & (fifa.Wage < 200)].count()[0]

plot = [very_high, high, medium, low]
labels = ('very high wage players', 'high wage players','medium wage players','low wage players')


plt.pie(plot, autopct='%.2f%%', labels=labels, startangle=65)
plt.show()













