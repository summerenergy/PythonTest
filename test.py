import numpy as np
def indect(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
x=np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])
y=np.array([[0,0,1,1]]).T
np.random.seed(1)
syno=2*np.random.rand(3,1)-1
for iter in xrange(10000):
    l0=x
    l1=indect(np.dot(l0,syno))
    l1_error=y-l1
    l1_date=l1_error*indect(l1,True)
    syno+=np.dot(l0.T,l1_date)
print l1
