# Plot the resulting signal with matplotlib. Calculate the FFT components of the signal and plot them.
from numpy import fft
import numpy as np
import matplotlib.pyplot as plt
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
print('\n fx \n', fx) 
fig, ax = plt.subplots()    #Ploting the resulting signal 
ax.plot(x, fx)
ax.set_xlabel('Time [f]')
ax.set_ylabel('Signal amplitude');
Fk = fft.fft(fx)/n # Fourier coefficients (divided by n)
nu = fft.fftfreq(n,dx) # Natural frequencies
Fk = fft.fftshift(Fk) # Shift zero freq to center
nu = fft.fftshift(nu) # Shift zero freq to center
f, ax = plt.subplots(3,1,sharex=True)
ax[0].plot(nu, np.real(Fk)) # Plot Cosine terms
ax[0].set_ylabel(r'$Re[F_k]$', size = 'x-large')
ax[1].plot(nu, np.imag(Fk)) # Plot Sine terms
ax[1].set_ylabel(r'$Im[F_k]$', size = 'x-large')
ax[2].plot(nu, np.absolute(Fk)**2) # Plot spectral power
ax[2].set_ylabel(r'$\vert F_k \vert ^2$', size = 'x-large')
ax[2].set_xlabel(r'$\widetilde{\nu}$', size = 'x-large')
plt.show()
