import numpy as np

#test_poly=np.array([[2,3.],[3,4.],[0,5.]])            ### (degree,frac coeff)

def cons(poly,co):
	c=np.where(poly[:,0]==0)[0]
	if np.size(c)!=0 :
		poly[c,1]=poly[c,1]-co
		return poly
	else:
		return np.concatenate((poly,[[0,-co]]),axis=0)

#print consc(test_poly,2.)
		

