import numpy as np
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# Query Protein
X = np.array([[0.517493,1.270000,0.902539,0.556603,0.894162,0.293138,0.087805,0.882027,0.998240,0.990514,0.985407,0.984260,0.970274,0.987151,1.614338,2.090359,0.107143,5.500000,0.277857,0.385000,-10.920558,0.942857,0.210000,0.390000,0.975714,-94.680426,0.967143,-93.875361,0.416429,-12.613706,0.778571,0.250000,0.440000,0.416429,-12.613706,0.778571,0.250000,0.460000,0.442857,0.700000,0.281317,0.837670,0.699767,0.651275,0.459507,0.118584,0.771014,0.551905,0.733474,0.610817,0.337149,0.917810,0.773046,0.804674,0.624112,0.314919,0.912910,0.757682,0.824398,0.664773,0.321779,0.000000,0.400000,0.600000,0.492857,0.507143,0.141732,0.401575,0.456693,0.566929,0.433071,0.975058,0.906225,0.796795,0.933690,0.843571,0.843571,0.767857,0.377143,0.360000,0.283571,1.872143,3.542857,-62.052662]] )
#minmax = list()
#stats = [[min(column), max(column)] for column in X


# Rescale dataset columns to the range 0-1
#for column in X:
 #   for i in range(len(column)-1):
  #      if minmax[1][i] != minmax[0][i]: 
   #         column[i] = (column[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
# output dataset            
y = np.array([[0]]).T

# seed random numbers to make calculation 
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((84,1)) - 1

for iter in range(10):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)
print ("Comparing the two proteins we get:\n",l1);