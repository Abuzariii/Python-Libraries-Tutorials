from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv("E:\Pyhton\Matplotlib\gas_prices.csv")
gas.loc[0, 'Australia']= 2
# print(gas.head(5))
plt.xlabel("Year")
plt.ylabel("Prices")
plt.xticks(gas.Year[::2])  #Xticks are seperated by 2 years each
plt.title("Gas Prices", fontdict={'fontweight': 'bold', 'fontsize':28})   #A bold title

#Use a for loop to get the entire file's graph
for country in gas:      #the columns can be named anything, we name them coutry here
    if country != 'Year':       
        plt.plot(gas.Year, gas[country], marker= '.', label= country)  

#If you want to pick few countries and graph them then use this method
countries_to_look_at = ['Australia', 'USA', 'Canada']
for country in gas:
    if country in countries_to_look_at:
        plt.plot(gas.Year, gas[country], marker= '.', label= country)




#Individually Plotting every country by gas price 
plt.plot(gas.Year, gas.France, label= "France", marker= '.')
plt.plot(gas.Year, gas['South Korea'], label= "South Korea", marker= '.')
plt.legend()
plt.show()
































