from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd

fifa = pd.read_csv("E:\Pyhton\Matplotlib\Fifa.csv")


plt.style.use('ggplot')
plt.title("Weight Distribution of FIFA Players")
#Converting all weights into integers so you can perform operations, stripping lbs from the weights 
fifa.Weight = [ x.strip('lbs') if type(x)==str else x for x in fifa.Weight]
fifa['Weight'] = fifa.Weight.astype(int)
# print(fifa.Weight[0]) #Print the first weight

light = fifa.loc[fifa.Weight <125].count()[0]
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight <150 )].count()[0]
medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight <175 )].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight <200 )].count()[0]
heavy = fifa.loc[(fifa.Weight >= 200)].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels= ['Under 125', '125-150', '150-175', '175-200', 'Over 200']

#Explode function splitts the circle areas, it goes in clockwise direction, you have to specify the distance
#Between the sections, 0 is default, increase it to get whatever you want
plt.pie(weights, labels=labels, autopct= '%0.2f%%', radius=1.4, explode=[0,0,0,0,0], startangle=0)
plt.show()


# weight_column = fifa[fifa.columns[27]]
# print(weight_column.head(5))   #Weight column 



