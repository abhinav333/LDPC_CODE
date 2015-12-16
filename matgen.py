#encodes parity check matrix into computational structure
#Each node is associated with a check node and a bit node
from cir_mat import *
import numpy as np

pmat=p_matrix  # parity check matrix



n_bits=[]   # bits_nodes-edge  list
n_checks=[]  # check_nodes-edge list

one_indices=np.where(pmat==1)   #acquire (edge,2) matrix containing 'one' indices
edge_no=one_indices[0].size

for y in range(0,pmat.shape[0]):
	n_checks.append(np.where(one_indices[0]==y)[0])  # sort check-nodes in terms of associated edges
for x in range(0,pmat.shape[1]):
	n_bits.append(np.where(one_indices[1]==x)[0]) #sort bit-nodes in terms of associated edges




	  
