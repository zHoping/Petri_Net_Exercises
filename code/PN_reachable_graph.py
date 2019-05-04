import numpy as np 
import pandas as pd
from graphviz import Digraph

def vextor2str(vector):
	string=''
	for i in np.arange(vector.size):
		string=string+str(int(vector[i,0]))
	return string

# read M_0, C_pre and C_post from excel file
C_pre=pd.read_excel('data.xls',sheet_name='C_pre',header=None) 
C_pre=np.array(C_pre)
C_post=pd.read_excel('data.xls',sheet_name='C_post',header=None)
C_post=np.array(C_post)
M_0=pd.read_excel('data.xls',sheet_name='M0',header=None)
M_0=np.array(M_0)
C=C_post-C_pre
P_num=C.shape[0]
T_num=C.shape[1]
# put M_0 into reachable_graph
reachable_graph=np.array([[0]])
new_states=[M_0]
new_states_num=1
# reachable states are saved in old_states list, orders in this list equal to orders in reachable_graph
old_states=[]
old_states_num=0
graph_states_num=1
print(reachable_graph)	
print('------------------')

while(new_states):
	#for any new_states, enable available transitions
	for i in np.arange(T_num):
		M_current=new_states[0]
		S=np.zeros([T_num,1])
		S[i,0]=1
		if((M_current>=np.dot(C_pre,S)).all()):
			M_current=M_current+np.dot(C,S)
			exist=False
			#if last state exists in old_states, not extend reachable_graph, link two states directly
			for j in np.arange(old_states_num):
				if((old_states[j]==M_current).all()):
					reachable_graph[old_states_num,j]=i+1
					exist=True
			#if last state exists in old_states, not extend reachable_graph, link two states directly
			for j in np.arange(new_states_num):
				if((new_states[j]==M_current).all()):
					reachable_graph[old_states_num,old_states_num+j]=i+1
					exist=True
			#if last state exists in old_states, extend reachable_graph, then link two states  
			if(exist==False):
				new_states.append(M_current)
				new_states_num=new_states_num+1
				reachable_graph=np.c_[reachable_graph,np.zeros(graph_states_num,dtype=int)]
				graph_states_num=graph_states_num+1
				reachable_graph=np.r_[reachable_graph,np.zeros((1,graph_states_num),dtype=int)]
				reachable_graph[old_states_num,graph_states_num-1]=i+1
			print(reachable_graph)	
			print('------------------')
	old_states.append(new_states.pop(0))
	new_states_num=new_states_num-1
	old_states_num=old_states_num+1

for i in np.arange(old_states_num):	
	print('M'+str(i)+': '+vextor2str(old_states[i]))

G=Digraph('test_picture')
for i in np.arange(old_states_num):
	G.node(vextor2str(old_states[i]))
for i in np.arange(old_states_num):
	for j in np.arange(old_states_num):
		if(reachable_graph[i,j]!=0):
			G.edge(vextor2str(old_states[i]),vextor2str(old_states[j]),'t'+str(reachable_graph[i,j]))
G.view()
