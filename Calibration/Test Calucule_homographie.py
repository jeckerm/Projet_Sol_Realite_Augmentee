import numpy as np
#Test build_A
print(build_A([[1,2],[3,4],[5,6],[7,8]]))

#Test build_b
print(build_b([[1,2],[3,4],[5,6],[7,8]]))

#Test build_H
#print(build_H(np.matrix([[1,2,3,4,5,6,7,8,9,10,11,12]])))

#Test homography
Lx =[[10,20],[35,41],[29,63], [53,69]]
LX =[[30, 65],[110,115],[81, 175], [150,210]]
H = homography(Lx,LX)
print(H)
print(H*np.matrix([[30],[65],[0],[1]]))