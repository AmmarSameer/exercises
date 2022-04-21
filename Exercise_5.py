# Make plots appear inline, set custom plotting style
from numpy import fft
import numpy as np
import matplotlib.pyplot as pyplot
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from numpy import where
from sklearn.datasets import make_classification

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
f11 = f1 + f2
f22 = f3 + f4 
ff = f11 ,f22

kmeans = KMeans(n_clusters=2, random_state=0).fit(ff)
kmeans.labels_
kmeans.predict(ff)
kmeans.cluster_centers_