####################### permute and connect edges ##########################
from hchk  import *
from matgen import *
from cir_mat import *
import numpy as np


### dummy codeword ###########
message=np.random.randint(2,size=20)        # make it  atwo dimensional array

code_p=np.remainder(np.matrix(message)*np.matrix(g_matrix),2)

### transmission noise
noise=np.zeros(code_p.shape)
noise[0,2]=np.remainder(code_p[0,2]+1,2)
noise[0,4]=np.remainder(code_p[0,4]+1,2)
noise[0,15]=np.remainder(code_p[0,15]+1,2)
noise[0,23]=np.remainder(code_p[0,23]+1,2)
code=np.remainder(code_p+noise,2)

##
edge_value=np.zeros(edge_no)
code_length=code.shape[1]
up_code=np.zeros((code_length,1)) ### initialitize code vector


## updating code and channel log ratios on each iteration
up_code[:]=code.T[:]


v_vect=n_bits     # fill vectors of bit node with matrix entries
u_vect=n_checks    #fill vectors connecting check nodes with corrsponding edges



iterations=30

### fill edge values with received codeword
for op in range(0,len(n_bits)):
	edge_value[n_bits[op]]=up_code[op]

for ier in range(0,iterations):
	
			
	for cc in range(0,len(n_checks)):
		temp_vect=edge_value[u_vect[cc]]
		temp2_vect=chk_c(temp_vect)
		edge_value[u_vect[cc]]=temp2_vect
	
	for bc in range(0,code_length):
		temp_vect=edge_value[v_vect[bc]]      #get edge values in temporary array
		temp2_vect,up_code[bc]=bit_c(temp_vect,up_code[bc])   # pass previous edge values 
		edge_value[v_vect[bc]]=temp2_vect #store updated value of edges
		
che_vector=code.T-up_code

### bit error rate calculation
errors=np.where(che_vector!=0)[0].size

print errors/np.float(up_code.size)   
plt.stem(che_vector)
plt.show();		
	











