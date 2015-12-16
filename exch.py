######### threshold analysis ##########################
import numpy as np
from cons import *
from nrm import *
import matplotlib.pyplot as plt

p_values=np.linspace(0.001,0.8,num=100)

last_val=0.0
thresh=0.0


bit_nodes=np.array([[3,1000]])        #### they define (degree,no of nodes of that degree)      #####tri(x) and P(x)
check_nodes=np.array([[6,500]])

##############  fractional node distribution (degree,fraction of nodes)

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

## for sweep
lambda_poly=np.zeros(bit_dist.shape)
lambda_poly[:,0]=b2_temp[:]
lambda_poly[:,1]=lambda_dist[:]


p_val_mat=[]
cxf_mat=[]
vpf_mat=[]
p=p_values[60]
#for p in p_values:
#	p_val=p 
  #### initialize with crossover 
ex_sweep=np.linspace(0.001,1.,200)
for xp in ex_sweep:
	cxf=1-np.sum(rho_dist*np.power(1-xp,c2_temp))
	cxf_mat.append(cxf)
	vpf=nrm_hall(cons(lambda_poly,xp/0.22),cxf,8)
	vpf_mat.append(vpf)

for p in p_values:
	p_val=p
	for ier in range(0,300):  ###### no of iteration of 
		q_val=1-np.sum(rho_dist*np.power(1-p_val,c2_temp))
		p_val=p*np.sum(lambda_dist*np.power(q_val,b2_temp))
			
	p_val_mat.append(p_val)
thresh=p_values[np.argmin(p_val_mat)]

print p_values[54]

print vpf_mat
plt.plot(vpf_mat)
plt.plot(cxf_mat)
plt.show()


		   





