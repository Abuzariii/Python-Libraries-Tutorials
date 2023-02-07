
#run all these methods seperately
import numpy as np

a = np.array([0,1,2,3,4,5])      #creation of an array using lists
print(a)

print(a.tolist())                #converting the numpy array to a python list


summedarray= a+2                           #generally adding an integer to every member of the array
print(summedarray)                         #it should work for all the arithmetic operators


appendedarray = np.append(a, 12)               #appending an element at the end
print(appendedarray)


insertedarray = np.insert(a,1,999)             #inserting any element at any index number, array name is followed by the  
print(insertedarray)                           # index number you want to insert at and the element you want to insert 


deletedarray = np.delete(a,3)                   #deleting a member at a specific index number
print(deletedarray)

b = np.delete(b, (0,5,9))                     #deleting multiple members at multiple indexes
print(b)

SlicedArray = a[2:5]                 #Slicing a subset array from one index to another
print(SlicedArray)

newSliced_a = a[-2:]                #slicing or extracting last two elements
print(newSliced_a)

np.savetxt("Practise CHarhgyi Lun p",a)     #savetext is a keyword that is used to save file in the directory

np.savetxt("practise.csv",a)               #this saves a csv file in your directory

a= np.arange(1,7)    #create an array withing given range
print(a)

print(a.shape)      #tells the shape of the array as number of rows and columns

b= a.reshape(2,3)   #reshaping the array to any number of rows and columsn.....will give error if the elements
print(b)            #are not sufficient

a= np.linspace(1,10,5, dtype=int)   #printing an array of given number of elements from one range to another
print(a)     #1 is start value, 10 is end value and 5 is the number of elements we want


a= np.random.randint(2,10, size=(2,3))  #create a random array of elements withing given range and of given
print(a)                                #size....2-10 is range of the values of the digits








