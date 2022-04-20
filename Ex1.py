# Make plots appear inline, set custom plotting style
from scipy import signal
import matplotlib.pyplot as plt
import random
import numpy as np
f1 = random.randint(1, 50)  # Sample rate of the periodic signal we will generate
f2 = random.randint(1, 50)  # Sample rate of the periodic signal we will generate
f3 = random.randint(1, 50)  # Sample rate of the periodic signal we will generate
f4 = random.randint(1, 50)  # Sample rate of the periodic signal we will generate
t1 = np.linspace(0, f1, 50 , False)        # Time duration of the signals 
t2 = np.linspace(0, f2, 50 , False)
t3 = np.linspace(0, f3, 50 , False)
t4 = np.linspace(0, f4, 50 , False)
s1 = np.sin(f1*np.pi*t1)                   # Generate signal with f1 amplitude and t1 Hz frequency 
s2 = np.sin(f2*np.pi*t2)                   # Generate signal with f2 amplitude and t2 Hz frequency
c1 = np.cos(f3*np.pi*t3)                   # Generate signal with f3 amplitude and t3 Hz frequency 
c2 = np.cos(f4*np.pi*t4)                   # Generate signal with f4 amplitude and t4 Hz frequency
su=s1+s2+c1+c2                  #total Signal
tt=t1+t2+t3+t4                  #total Time
print( su)             #A numpy array that contains a periodic signal, which is generated from the sum of two sine and two cosine functions. The frequency and amplitude of the sine and cosine components are arbitrary
