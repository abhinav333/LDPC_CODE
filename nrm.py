import numpy as np

#test_poly=np.array([[2,1.],[1,2.],[0,1.]])  ## polynomial(degree,coefficient)

def nrm_hall(poly,initial=0.,cn=5):

	poly_dt=np.zeros(poly.shape)        ## 1st derivative   
	poly_dt[:,0]=poly[:,0]-np.ones(poly.shape[0])
	poly_dt[:,1]=poly[:,0]*poly[:,1]
	de=np.where(poly_dt[:,0]<0)[0]
	poly_d=np.delete(poly_dt,de,0)



	poly_d2t=np.zeros(poly_d.shape)
	poly_d2t[:,0]=poly_d[:,0]-np.ones(poly_d.shape[0])
	poly_d2t[:,1]=poly_d[:,0]*poly_d[:,1]
	de2=np.where(poly_d2t[:,0]<0)[0]
	poly_d2=np.delete(poly_d2t,de2,0)


	t=1.
	rs=initial
	while np.absolute(t)>np.power(10.,-cn):
		fx=np.sum(np.power(rs,poly[:,0])*poly[:,1])
		fxd=np.sum(np.power(rs,poly_d[:,0])*poly_d[:,1])		
		#mxd2=np.sum(np.power(rs,poly_d2[:,0]*poly_d2[:,1]))
		if (fxd!=0):
			t=(fx/fxd)                             #n method 
		rs=rs-t                                       # n method
		#	t=(fx/(fxd-((fx*fxd2)/(2*fxd))))      ##h method
		#rs=rs-t                                      ## h method
		#rs=np.around(rs,decimals=4)
	return rs



