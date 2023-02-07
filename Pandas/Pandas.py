import pandas as pd
import numpy as np            #using numpy array as pandas

#Pandas syntax goes from columns to rows

dic1 = {
    "Names": ['Abuzar','Rafay', 'Uzair', 'Eeshal'],
    "Courses": ['Software Engg', 'Computer  Sc', 'FSc', 'MBBS'],
    "Cities": ['Chishtian', 'Ryk', 'Maansehra', 'Daska']
}

        # Data Writing
Data = pd.DataFrame(dic1)
print(Data)

a = pd.DataFrame(dic1)   
print(a.Name)       #Accessing any column in pandas data frame




Data.to_csv("Monkes.csv", index=False)
print(Data.describe())


         #Data Reading
data = pd.read_csv('Monkes.csv')
print(data)

df = pd.read_csv('D:\Snapchat\Snapchat\Monkes.csv', index_col=0) #Read csv files without indeces


df = pd.DataFrame(data, columns= ['Courses'])
print (df)
               


               #Using numpy array as data in pandas
#Pandas display data in a spreadsheet form numpy does it in matrix form
# you can convert a numpy array in a panda spreadhseet or vice versa               
a = np.array(([1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]))       
b = pd.DataFrame(a)      #converting a numpy array into a panda data frame 
print(b)

print(b.drop(0, axis=0))    #To drop a column or a row, use this, axis=0 is row and axis=1 is column

b.columns = list("ABCD")   #Change the names of all column headers, or assigning names by yourself
b.columns = list(['A', 'B','C','D','E','F'])   #change column headers to whatever name u want

b.index = list(['A', 'C', 'D', 'E', 'F', 'G'])   #Changing names of rows

df.loc['X']= [12,14,11,121,1,2,3,4]   #Changing the values of an entire row

df.index = list("ABC")     #Change the names of all column headers, or assigning names by yourself


df = DataFrame(index=['A', 'B', 'C'], columns=['x', 'y'])    #Creating a panda data gframe of your own choice
print(df)              #of rows and columns

df.loc['A', 'x']= 12    #Changing any value, use loc keyword followed by row name and column name
print(df)

df.loc['A', 'x']= 'Abuzar'  #Pandas can change the value to both string or integer
print(df)

print(df.reset_index(drop=True))  #Resetting the rows names and turn them into indexes

df['B']= None     #Turning the members of a row into none
print(df)

print(df.min(axis=1))   #get the minimum value in a row, use index = 0 for columns

print(b.loc[[1,2], ["A", "B"]])  #slicing , enter the row number and then the column names
print(b.loc[[1,2], [1,2]])     #Slicing the rows and columns if they are not named
        #Use names if they are named or use indexes if they are only indexed
print(b.loc[[1,2], :])   #to slice a some rows and all columns , and vice versa


print(b.iloc[3,2])    #Index Location, Accessing any single element using index of row and column
print(b.loc[3,"C"])    #Location using names of the rows and columns

print(b.head(3))   #Printig first three rows of a data frame
print(b.tail(2))   #Printing last two rows of a dta frame

print(df[df.columns[0:4]])   #Accessing any number of columns you want

