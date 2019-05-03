import numpy as np 
import pandas as pd
import random as rd

# read M_0, C_pre and C_post from excel file
C_pre=pd.read_excel('data.xls',sheet_name='C_pre',header=None) 
C_pre=np.array(C_pre)
C_post=pd.read_excel('data.xls',sheet_name='C_post',header=None)
C_post=np.array(C_post)
M_0=pd.read_excel('data.xls',sheet_name='M0',header=None)
M_0=np.array(M_0)
M_current=M_0
print(M_current)
C=C_post-C_pre
P_num=C.shape[0]
T_num=C.shape[1]
round=10 #set runtime

while(round>0):
	round=round-1
	# if a transition is available, add this transition into available_T list
	available_T=[] 
	for i in np.arange(T_num):
		S=np.zeros([T_num,1])
		S[i,0]=1
		if((M_current>=np.dot(C_pre,S)).all()):
			available_T.append(i)
	# if there are any transition in available_T list, choose one to enable
	if(len(available_T)>0):
		S=np.zeros([T_num,1])
		S[available_T[rd.randint(0,len(available_T)-1)],0]=1
		M_current=M_current+np.dot(C,S)
		print('---------')
		print(M_current)

