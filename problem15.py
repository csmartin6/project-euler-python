import numpy as np

N=20

num_paths = np.zeros((N+1,N+1),dtype=int)

num_paths[0,:]=1
num_paths[:,0]=1

for i in range(1,N+1):
	for j in range(1,N+1):
		from_left = num_paths[i,j-1]
		from_above = num_paths[i-1,j]
		num_paths[i,j] = from_left+from_above

print num_paths[-1,-1]

cache={}
def countRoutes(i,j):
	if i==0 or j==0:
		return 1
	else:
		if (i,j) in cache:
			return cache[(i,j)]
		else:
			cache[(i,j)] = countRoutes(i-1,j)+countRoutes(i,j-1)
			return cache[(i,j)]

print countRoutes(20,20)
