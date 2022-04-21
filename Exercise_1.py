#Create a numpy array that contains a periodic signal, which is generated from the sum of two sine and two cosine functions. The frequency and amplitude of the sine and cosine components are arbitrary.
import numpy as np
n = 1000                    # Number of data points
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
print('\n fx \n', fx)             #A numpy array that contains a periodic signal, which is generated from the sum of two sine and two cosine functions. The frequency and amplitude of the sine and cosine components are arbitrary
