import numpy as np

#1.1) 2 x 3
#1.2) 2 x 2
#1.3) 3 x 2
#1.4) 2 x 3
#1.5) 1 x 4
#1.6) 4 x 1

#2)
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

#2.1) 
u + v # [9,  7, -4,  9]
#2.2) 
u - v # [3, -3, -2,  1]
#2.3) 
6 * u # [36,  12, -18,  30]
#2.4) 
np.dot(u,v) # 51
#2.5) 
np.sqrt(np.dot(u,u)) # 8.6023252670426267

#3)
A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])

#3.1) 
# A + C is not defined
#3.2) 
A - C.T # [[-4, -7, -3], [3, 6, 4]]
#3.3) 
C.T + 3*D # [[14, 3, 3], [2, 7, 9]]
#3.4) 
B*A # [[-1, -5, -1], [2, 7, 4]]
#3.5)
# B*A.T is not defined
#3.6) 
# B*C is not defined
#3.7) 
C*B # [[5, -6], [9, -8], [6, -6]]
#3.8) 
B**4 # [[1, -4], [0, 1]]
#3.9) 
A*A.T # [[14, 28], [28, 69]]
#3.10) 
D.T*D # [[10, -4, 0], [-4, 8, 8], [0, 8, 10]]
