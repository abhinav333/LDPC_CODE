import numpy as np

a_mat=np.array( [
			[1,1,0],
			[1,0,1],
			[0,1,1],
			[1,1,1]
		])

code_length=np.int(7)
info_bits=np.int(4)
gen_matrix=np.matrix(np.concatenate((np.identity(info_bits),a_mat),axis=1))
hamm_matrix=np.matrix(np.concatenate((a_mat.T,np.identity(code_length-info_bits)),axis=1))

m=np.matrix([1,0,1,1])
div_mat=2*np.ones((1,code_length),dtype=np.int)
code=np.mod(m*gen_matrix,div_mat)
print(code.astype(np.int))

######## decoding         ##############		
### tamper the code

############################33
div_mat2=2*np.ones((code_length-info_bits,1),dtype=np.int)

code=np.matrix(code)
syn_mat=np.mod((hamm_matrix*code.T),div_mat2)
print(syn_mat.astype(np.int))
print '\n'
print(hamm_matrix*gen_matrix.T)

