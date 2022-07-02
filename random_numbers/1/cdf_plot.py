#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,4,60)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
def cduniform2(x):
    if (x<=0):
       return 0
    elif (x>=0 and x <=1):
       return x
    else:
       return 1
    
theoritical = []
for i in range(len(x)):
   theoritical.append(cduniform2(x[i]))
plt.plot(x,err,'x')#plotting the CDF
plt.plot(x,theoritical)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.show() #opening the plot window
