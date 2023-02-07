from pathlib import PureWindowsPath
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fifa = pd.read_csv("E:\Pyhton\Matplotlib\Fifa.csv")

plt.title("Team COmparison Box Plots")
plt.style.use("default")
plt.figure(figsize=(5,8))

#From the club column we are printing overalls of FC Barcelona, Madrid and Juventus Players
barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club =='Real Madrid']['Overall']
juventus = fifa.loc[fifa.Club== 'Juventus']['Overall']

labels = ["FC Barcelona", "Real Madrid", "Juventus"]
plt.ylabel("FIFA Overall Ratings")

boxes = plt.boxplot([barcelona, madrid, juventus], labels= labels)


#Setting color for all  boxes, outside and inside
for box in boxes['boxes']:
    box.set(color='pink', linewidth= 2)
    # box.set(facecolor='black', patch_artist=True)


plt.show()

