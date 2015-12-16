import numpy as np

def cal_llr(num,po):
	if num==0 :
		return(np.log((1-po)/po))
	elif num==1 :
		return(np.log(po/(1-po)))




