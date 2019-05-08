import numpy as np 
import pandas as pd
import random as rd
from graphviz import Digraph

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

def num2token(num):
	string=''
	for i in np.arange(num):
		string=string+'O'
	return string

def plot_PN(fire_T,round,T_num,P_num,M_current,C_pre,C_post):
	G=Digraph(str(round))
	for i in np.arange(T_num):
		G.node('t'+str(i+1),shape='rect',height='0')
	if (fire_T!=0):
		G.node('t'+str(fire_T),shape='rect',height='0',color='red')
	for i in np.arange(P_num):
		G.node('P'+str(i+1),label='P'+str(i+1)+'\n'+num2token(M_current[i,0]),shape='circle',height='1')
	for i in np.arange(T_num):
		for j in np.arange(P_num):
			if(C_pre[j,i]==1):
				G.edge('P'+str(j+1),'t'+str(i+1))
			if(C_post[j,i]==1):	
				G.edge('t'+str(i+1),'P'+str(j+1))
	G.view()


round=0 #set runtime
plot_PN(0,round,T_num,P_num,M_current,C_pre,C_post)
while(round<10):
	round=round+1
	# if a transition is available, add this transition into available_T list
	available_T=[] 
	for i in np.arange(T_num):
		S=np.zeros([T_num,1])
		S[i,0]=1
		if((M_current>=np.dot(C_pre,S)).all()):
			available_T.append(i)
	# if there are any transition in available_T list, choose one to enable
	if(available_T):
		S=np.zeros([T_num,1])
		fire_T=rd.randint(0,len(available_T)-1)
		S[available_T[fire_T],0]=1
		M_current=M_current+np.dot(C,S)
		print('-----t'+str(available_T[fire_T]+1)+'-----')
		print(M_current)
		plot_PN(available_T[fire_T]+1,round,T_num,P_num,M_current,C_pre,C_post)
