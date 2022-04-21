# Make plots appear inline, set custom plotting style
from numpy import fft
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

import matplotlib.pyplot as plt
n = 100                    # Number of data points
dx = 5.0                    # Sampling period (in meters)
x = dx*np.arange(0,n)       # x coordinates
w1 = 100.0                  # wavelength (meters)
w2 = 20.0                   # wavelength (meters)
w3 = 60.0
w4 = 30.0
f1=  6*np.sin(2*np.pi*x/w1)  
f2=  2*np.cos(2*np.pi*x/w2)
f3=  3*np.sin(2*np.pi*x/w3)
f4=  5*np.cos(2*np.pi*x/w4)
fx = f1 + f2+f3+f4 # signal
#print('\n fx \n', fx) 
fig, ax = plt.subplots()    #Plot the resulting signal 
ax.plot(x, fx)
ax.set_xlabel('Time [f]')
ax.set_ylabel('Signal amplitude');

noise = np.random.normal(0, 1, 100)      # 0 is the mean of the normal distribution you are choosing from
                                         # 1 is the standard deviation of the normal distribution
                                         # 100 is the number of elements you get in array noise
new_signal = fx + noise                  # adding noise to the original signal 


fig, bx = plt.subplots()                 #Ploting the resulting signal 
bx.plot(x, new_signal)
bx.set_xlabel('Time [f]')
bx.set_ylabel('Signal amplitude');
bx.set_ylabel(r'$new_signal$', size = 'x-large')

fxs=(fx - np.min(fx)) / (np.max(fx) - np.min(fx)) #Standardize of the original signal
fxn=(new_signal - np.min(new_signal)) / (np.max(new_signal) - np.min(new_signal)) #Standardize the resulting signal
print('\n fxs \n', fxs)
fig, ax = plt.subplots()                 #Ploting the Standardize of the original signal 
ax.plot(x, fxs)
ax.set_xlabel('Time [f]')
ax.set_ylabel('Signal amplitude');
ax.set_xlabel(r'$Standardize the original signal$', size = 'x-large')

fig, ax = plt.subplots()                 #Ploting the Standardize of the original signal 
ax.plot(x, fxn)
ax.set_xlabel('Time [f]')
ax.set_ylabel('Signal amplitude');
ax.set_xlabel(r'$Standardize the resulting signal$', size = 'x-large')