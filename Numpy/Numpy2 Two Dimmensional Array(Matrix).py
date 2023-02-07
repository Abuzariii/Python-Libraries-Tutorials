import numpy as np

a = np.array(([1,2,3], [4,5,6], [7,8,9]))     #multiple lists that print out as a matrix

print(a)

print(np.size(a))                             #tells us the number of elements in the array


new_array = np.delete(a,0, axis=0)       # two dimensional arrays has rows as axis 0 and columns as axis 1
print(new_array)                         #we are using delete function to delete a row


new_array2 = np.delete(a,0, axis=1)      #here we are deleting a column
print(new_array2)

print(a[1,2])     #indexing a specific element, enter the index of row and then the column


print(np.append(a,0))     #append flattens the matrices into an array and adds the number in the end

dot_product = a@b           #dot product of two matrices
print(dot_product)

print(a.T)    #Transpose

print(np.linalg.det(a))    #to find determinant    use linalg keyword to see more matrix functions

print(np.diag(a))      #to find diagonal

print(a[1:2,1:3])      #to slice any number of elements, input its rows and columns indexes

boolindex = a>2    #Boolean indexing gives the entire 2 dimensional array with values as true or false
print(boolindex)

print(a[a>2])      #boolean inexing gives the entire matrix with only those elements that meet the condition

b= np.where(a>2,a,0)    #where method is used to create a new matrix that puts a new value at positions
print(b)                # the condition isnt met    (this program will put 0 at those positions)

a= np.array([1,2,3,4,5,6,7,8,9])    #fancy indexing using a list....create a list of indexes you want to
b=[1,5,7]                           #print and print the array using the list
print(a[b])

odd =  np.argwhere(a%2!=0)   #applying a condition and printing only those elements who meet it
print(a[odd])

odd =  np.argwhere(a%2!=0).flatten()  #above program will print a 2 dimesional array but use flatten
print(a[odd])                         #keyword to get a unidimensional array

a= np.array([[1,2,3]])      #concatenate two or more arrays , remember use double [] to get two dimesnional
b= np.array([[4,5,6]])      #array, or use double () to get a uni dimensioanl concatenated array
c= np.concatenate((a,b))
print(c)

a= np.array([[1,2,3]])   #concatenation and do the same thing as above but using axis keyword
b= np.array([[4,5,6]])    # remember it is for matching dimesnions if dimesnions dont match you will get error
c= np.concatenate((a,b), axis=0)
print(c)

a= np.array([[1,2,3]])   #stacking two arrays horizontally
b= np.array([[4,5,6]])
c= np.hstack((a,b))
print(c)

a= np.array([[1,2,3]])   #stacking two arrays vertically
b= np.array([[4,5,6]])
c= np.vstack((a,b))
print(c)

###### Data Science functions on arrays

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))     #sum of rows
print(a)
print(a.sum(axis=0))

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))    #sum of columns
print(a)
print(a.sum(axis=1))

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))    #sum of all the elements
print(a)
print(a.sum(axis=None))

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))  #find the mean on rows
print(a)
print(a.mean(axis=0))                    #change axis to 1 to find mean on columns


a= np.array(([1,2,3,4,5],[6,7,8,9,10]))  #general mean or arithmetic mean
print(a)                                 #sum of all the members divided by the number of members
print(a.mean(axis=None))

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))   #Standard Deviation
print(a)
print(a.std(axis=None))

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))    #Variance
print(a)
print(a.var(axis=None))

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))  #General minimum value
print(a)
print(a.min(axis=None))

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))   #row with minimum values
print(a)
print(a.min(axis=0))

a= np.array(([1,2,3,4,5],[6,7,8,9,10]))    #column with minimum values
print(a)
print(a.min(axis=1))



a= np.zeros((2,2), dtype=int)     #Printing a Zero Matrix
print(a)


a= np.ones((2,2), dtype=int)      #Printing a ones matrix
print(a)

a= np.full((2,2), 12)      #creating an array of any dimension with any element 
print(a)

a= np.eye((3), dtype=int)    #an identity matrix of 3 rows and 3 columns
print(a)


np.set_printoptions(precision=2, suppress=True)   #any array printed after this will have only 2 digits after decimal point





































