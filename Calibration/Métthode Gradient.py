import numpy as np



A= np.matrix([[1],[1],[0],[1],[0],[0],[1],[0],[1],[1],[1],[1]])
print(A)
print(int(A[3][0]))
B=A.copy()
print(B)
C=np.eye(3,12)
print(C)
print(len(C))
print(len(C[0]))

def gradient(M,H):
    n = len(M)
    p = len(H)
    N = np.eye(n,p)
    for i in range (0,n):
        for j in range(0,p):
            if i==n-1 and j=p-1:
                N[i][j] = (int(M[i+1])-int(M[i]))/(int(H[i+1])-int(H[i]))
                
            N[i][j] = (int(M[i+1])-int(M[i]))/(int(H[i+1])-int(H[i]))
    
    
    
    