#最近邻  
import numpy as np    
from numpy import linalg as la    
from sklearn.neighbors import NearestNeighbors    
M=np.array(["你吃饭了吗","今天的花儿很好看","简直不能更完美","你喜欢吃辣椒吗","天气很完美","这个花儿长的像辣椒"])  
X = np.array([[-1,-1],    
              [-2,-1],    
              [-3,-2],    
              [1,1],    
              [2,1],    
              [3,2]    
              ])    
nbrs = NearestNeighbors(n_neighbors=3, algorithm="ball_tree").fit(X)    
#返回距离每个点k个最近的点和距离指数，indices可以理解为表示点的下标，distances为距离    
distances, indices = nbrs.kneighbors(X)      
print(indices[4])  
for i in indices[4]:  
    print(M[i])  