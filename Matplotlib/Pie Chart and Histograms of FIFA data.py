from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

       
Fifa = pd.read_csv("E:\Pyhton\Matplotlib\Fifa.csv")

#      #Pie Chart
plt.title("Foot Preference of FIFA Players")  


left = Fifa.loc[Fifa['Preferred Foot']=='Left']  #Printing the left footed players only with all the attributes

left = Fifa.loc[Fifa['Preferred Foot']=='Left'].count()[0]   #Print the number of left footed players
right = Fifa.loc[Fifa['Preferred Foot']=='Right'].count()[0]

#autopct to show percentage and .5f is to use how many digits of float you want, u can use i for int
plt.pie([left, right], labels=['Left', 'Right'], colors=['red', 'pink'], autopct= '%.2f%%')
plt.show()



#      #Histogram
plt.title("Distribution of player skills in fifa 2021")
plt.ylabel("Number of players")
plt.xlabel("Skill Level")
overalls = [0,10,20,30,40,50,60,70,80,90,100]
plt.xticks(overalls)

#bins are basically blocks in a histogram
#you can set their limits in a list and the use bin= to use them
plt.hist(Fifa.Overall, bins=overalls, color='Pink')

plt.show()