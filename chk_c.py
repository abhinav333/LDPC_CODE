
import numpy as np


###########check point log likelihood calculation ############################
def chk_c(arr):
	llr=np.log(np.tanh(arr/2.))
	su=np.sum(llr)
	u_vect=np.zeros(llr.size)
	for it in range(0,llr.size):
		 u_vect[it]=su-llr[it]			
	u_vect_llr=2*np.arctanh(np.exp(u_vect))
	return(u_vect_llr)
####################bit node likelihood calculation ###########################
def bit_c(uvecs,li):
	su1=np.sum(uvecs)+li
	v_vect=np.zeros(uvecs.size)
	for uit in range(0,uvecs.size):
		v_vect[uit]=su1-uvecs[uit]
	return v_vect,su1

		

	

