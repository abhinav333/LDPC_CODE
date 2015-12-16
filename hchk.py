
import numpy as np


###########check point calculation ############################
def chk_c(arr):

        xr=0;
	for sw in range(0,arr.size):
		xr=np.logical_xor(xr,arr[sw])
	
	u_vect=np.zeros(arr.size)
	for it in range(0,arr.size):
		 if np.logical_xor(xr,arr[it])==True:
			 u_vect[it]=1
	
	return(u_vect)
####################bit node  calculation ###########################
def bit_c(uvecs,ini):
        re=ini
	if np.where(uvecs==0)[0].size==uvecs.size:
		re=0
	elif np.where(uvecs==1)[0].size==uvecs.size:
		re=1
	 	 
	v_vect=np.zeros(uvecs.size)


	for uit in range(0,uvecs.size):
		temp=np.delete(uvecs,uit)
		if temp.size!=0	:
			if np.where(temp==1)[0].size==temp.size:
				v_vect[uit]=1
			elif np.where(temp==0)[0].size==temp.size:
				v_vect[uit]=0
			else:v_vect[uit]=ini	
		else: v_vect[uit]=ini
	return v_vect,re

		


