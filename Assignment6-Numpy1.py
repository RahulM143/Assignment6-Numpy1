#Problem Statement 1:
##Write a function so that the columns of the output matrix are powers of
#the input vector.
#The order of the powers is determined by the increasing boolean argument. 
#Specifically,when increasing is False, the i-th output column is the 
#input vector raised element-wise to the power of N - i - 1.

#HINT: Such a matrix with a geometric progression in each row is named 
#for Alexandre- Theophile Vandermonde.
#x = np.array([1, 2, 3, 4,5])
#len(x)
#y = np.vander(x, increasing = False)
#y
import numpy as np 
def van (a,n,inc): # function for Vander progression
   if inc == 'True': 
       i = n-1
       while i >= 0:
           a[:,n-i-1]**=(n-i-1)
           i -=1
       return a
   else:
       i = n-1
       k= 1
       while i >=0:
           a[:,n-i-1]**= (n-k)
           i -=1
           k = k + 1
       return a
num = [1,2,3,4,5]
print ('Input list of numbers is: ', num)
length = len (num) # count of inputs in the list
length
in_arr = np.array(num).reshape(length,1)
in_arr # converted to array
zer_arr = np.zeros((length,length)) # square matrix of zeroes
zer_arr
com_arr = zer_arr + in_arr
com_arr # Matrix of 5,5 

inc_param = input('Select parameter for increasing (True/False): ',)
inc_param 
alex_vander = van (com_arr,length,inc_param)
print('\nAlex Vandermonde matrix with parameter as',inc_param, 'is \n', alex_vander)














