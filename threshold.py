######### threshold analysis ##########################
import numpy as np

p_values=np.linspace(0.001,0.1,num=100)

last_val=0.0
thresh=0.0

####### p_edge or q_edge=([degree,prob distribution]) ##########3
bit_dist=np.array([[3,1.]])
check_dist=np.array([[6,1.]])

b_temp=np.array(bit_dist[:,0]*bit_dist[:,1])
c_temp=np.array(check_dist[:,0]*check_dist[:,1])

c2_temp=check_dist[:,0]-np.ones(check_dist.shape[0])
b2_temp=bit_dist[:,0]-np.ones(bit_dist.shape[0])

pi_dist=np.array(b_temp/np.sum(b_temp))
rho_dist=np.array(c_temp/np.sum(c_temp))





p_val_mat=[]

for p in p_values:
	p_val=p   #### initialize with crossover 
	for ier in range(0,300):  ###### no of iteration of 
		q_val=np.sum(rho_dist*(1-np.power((1-2*p_val),c2_temp)))/2.
		p_val=np.sum(pi_dist*((1-p)*np.power(q_val,b2_temp)+p*(1-np.power(1-q_val,b2_temp))))
		
	p_val_mat.append(p_val)
thresh=p_values[np.argmin(p_val_mat)]
print p_val_mat





		   





