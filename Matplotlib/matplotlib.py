from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd


#Fontdict can be used in both title and  both labels 
plt.title("My First Graph", fontdict={'fontname': 'MS Gothic', 'fontsize': 20, 'fontweight': 'bold'})
style.use("fivethirtyeight")    #Graph Styles like ggplot , classic, Solarize_Light2, seaborn, default
plt.xlabel("X")
plt.ylabel("Y")
x= [1,2,3]    #dimensions of x and y must be same
y = [4,5,6]
plt.xticks([1,2,3])       #Xticks to int or anything u want
plt.yticks([4,5,6])       #ticks specify the value, it wont use default way

plt.figure(figsize=(3,3), dpi=200)    #resizing and putting pixels per inch, size is arbitrary

#Label name plus the line width and line color, marker and its size and its edge color, linestyle
plt.plot(x,y, label='TheLine', linewidth = 2, color = 'black', marker = ".", markersize=15, markeredgecolor = 'red', linestyle = '--')
# plt.plot(x,y , "r.--")  #Smart way of doing it, color intial then marker and then line
plt.legend()     #If you want a legend....always use it under the plotting
print(plt.show())








             #CREATING BARS

labels = ['A', 'B', 'C', 'D']
values = [1,2,3,4]
bars =plt.bar(labels, values, color=['black', 'red', 'green', 'blue', 'cyan'])

bars[2].set_hatch('o')
bars[0].set_hatch('|')        #one way of individually giving a hatch to every bar
bars[1].set_hatch('*')

patterns = ['o', '*', '|', '/']   #convenient way of using loop to provide a hatch to every bar
for bar in bars:
    bar.set_hatch(patterns.pop())

plt.show()

































