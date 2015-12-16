######### threshold analysis ##########################
import numpy as np

p_values=np.linspace(0.001,0.8,num=100)

last_val=0.0
thresh=0.0


bit_nodes=np.array([[3,1000]])        #### they define (degree,no of nodes of that degree)      #####tri(x) and P(x)
check_nodes=np.array([[6,500]])

##############  fractional node didtribution (degree,fraction of nodes

bit_dist=np.zeros(bit_nodes.shape)
bit_dist[:,0]=bit_nodes[:,0]
bit_dist[:,1]=bit_nodes[:,1]/np.sum(bit_nodes[:,1])            #### r(x) and  l(x)

check_dist=np.zeros(check_nodes.shape)
check_dist[:,0]=check_nodes[:,0]
check_dist[:,1]=check_nodes[:,1]/np.sum(check_nodes[:,1])


######## fractional edge distribution

b_temp=np.array(bit_dist[:,0]*bit_dist[:,1])                         ### rho(x) and pi(x)
c_temp=np.array(check_dist[:,0]*check_dist[:,1])

########### degree -1 matrix
c2_temp=check_dist[:,0]-np.ones(check_dist.shape[0])
b2_temp=bit_dist[:,0]-np.ones(bit_dist.shape[0])

lambda_dist=np.array(b_temp/np.sum(b_temp))
rho_dist=np.array(c_temp/np.sum(c_temp))





p_val_mat=[]
p=p_values[60]
for p in p_values:
	p_val=p 
  #### initialize with crossover 
	for ier in range(0,300):  ###### no of iteration of 
		q_val=1-np.sum(rho_dist*np.power(1-p_val,c2_temp))
		p_val=p*np.sum(lambda_dist*np.power(q_val,b2_temp))
			
	p_val_mat.append(p_val)
thresh=p_values[np.argmin(p_val_mat)]

print p_values[54]





		   





