import numpy as np
np.random.seed(0)
x,y=sklearn.datasets.make_moon(200,noise=0.20)
plt.scatter(x[:,0],x[:,1],s=40,c=y,cmap=plt.cm.Spectral)
