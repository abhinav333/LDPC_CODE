#creates a circulant matrix of order n x m
import matplotlib.pyplot as plt
from scipy.linalg import circulant
import numpy as np
import math
def cir_mat(arry):
	return np.array(circulant(arry)).T

# generalize
code_l=30
n_circ=3
circ_size=10


matr=np.zeros((n_circ,circ_size,circ_size))
p_matrix=np.zeros((circ_size,circ_size))

#matr[0]=cir_mat([1,1,0,0,0])
#matr[1]=cir_mat([1,0,1,0,1])

#p_matrix[:]=matr[0,:,:]
#p_matrix=np.concatenate((p_matrix,matr[1]),axis=1)
#print p_matrix



tempmat=np.array([[1,0,0,0,0,0,0,1,0,0],\
[0,0,1,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0]])

     # randomized
for jo in range(0,n_circ):
	matr[jo]=cir_mat(tempmat[jo])
	if jo==0:
		p_matrix=matr[jo]
	else:
        	p_matrix=np.concatenate((p_matrix,matr[jo]),axis=1)

# creating generator matrix for coding

i_mat=np.identity(circ_size*(n_circ-1))

matg=np.zeros((n_circ-1,circ_size,circ_size))
deti=np.linalg.det(matr[matr.shape[0]-1])
inv_mat=np.linalg.inv(matr[matr.shape[0]-1])*deti
inv_mat=np.remainder(np.absolute(inv_mat),2) 


g1_matrix=np.zeros((circ_size,circ_size))
for ajo in range(0,matr.shape[0]-1):
	matg[ajo]=(cir_mat(np.remainder((np.matrix(inv_mat)*np.matrix(matr[ajo]))[0,:],2))).T
	if ajo==0:
		g1_matrix=matg[ajo]
	else:	
		g1_matrix=np.concatenate((g1_matrix,matr[ajo]),axis=0)

g_matrix=np.concatenate((i_mat,g1_matrix),axis=1)
	 


#pirint np.matrix(g_matrix)*np.matrix(p_matrix).T	

 




#plt.imshow(inv_mat,cmap='Greys',interpolation='nearest')
#plt.show()

