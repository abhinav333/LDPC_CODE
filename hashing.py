####################### permute and connect edges ##########################
from  chk_c import *
from ini_llr import *
import numpy as np


### dummy codeword ###########
##code=np.array([[1,0,1,0]])   make it  atwo dimensional array


po=0.6   ############################ channel flip probability #####################
code_length=np.int(200)
check_nodes=np.int(10)
bit_degree=np.int(5)

edge_no=np.int(code_length*bit_degree)
### for regular codes only ###########
check_degree=np.int((code_length*bit_degree)/bit_degree)

edge_value=np.zeros(edge_no)

up_code=np.zeros((code_length,2)) ### calculates initial llr values


## updating code and channel log ratios on each iteration
up_code[:,0]=code.T[:]
up_code[:,1]=call_llr(up_code[:,0],po)

############ v_vect=      fill vectors of bit node with matrix entries
############ u_vect=      fill vectors connecting check nodes with corrsponding edges

iterations=np.int(10)

while iterations>0:
	for bc in range(0,code_length):
		temp_vect=edge_value[v_vect[bc]]      #get edge values in temporary array
		temp2_vect=bit_c(temp_vect,up_code[bc,1])   # pass previous edge values with channel llr
		edge_value[v_vect[bc]]=temp2_vect #get updated value of edges
		if (np.sum(temp2_vect)+up_code[bc,1])>0 :
			up_code[bc,0]=0
		else
			up_code[bc,0]=1
			
	for cc in range(0,check_nodes):
		temp_vect=edge_value[u_vect[cc]]
		temp2_vect=chk_c(temp_vect)
		edge_value[u_vect[cc]]=temp2_vect
	
	iterations-=1
	










