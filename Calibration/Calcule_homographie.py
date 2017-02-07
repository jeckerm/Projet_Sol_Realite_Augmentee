def optimize(A,b, x0=None,eps0=None, eps1=None, kmax=None):
    return(np.linalg.inv(A)*b)


def build_A(LX):
    #Lx rassemble l'ensemble des coordonnées des points sur l'écran sous la forme: Lx = [[x1,y1],[x2,y2]...]
    #LX rassemble l'ensemble des coordonnées des points mesurés sur le sol sous la forme: LX = [[X1,Y1],[X2,Y2]...]
    p=len(LX)
    A=np.matrix(np.zeros((3*p,12)))
    for t in range(0,3):
        for i in range(0,p):
            for j in range(0,2):
                A[p*t+i,j+4*t]=LX[i][j]
            A[p*t+i,2+4*t]=0
            A[p*t+i,3+4*t]=1
    return(A)

def build_b(Lx):
    p=len(Lx)
    L=[]
    for j in range(0,2):
        for i in range(0,p):
            L.append(Lx[i][j])
    l=[0 for i in range(0,p)]
    L=L+l
    return(np.matrix(L))
    
def build_H(h):
    p = np.size(h)
    H=np.matrix(np.zeros((3,4)))
    for i in range(0,3):
        for j in range(0,4):
            H[i,j] = h[0, 4*i+j]
    return(H)
    

def homography(Lx,LX):
    #Lx rassemble l'ensemble des coordonnées des points sur l'écran sous la forme: Lx = [[x1,y1],[x2,y2]...]
    #LX rassemble l'ensemble des coordonnées des points mesurés sur le sol sous la forme: LX = [[X1,Y1],[X2,Y2]...]
    A=build_A(LX)
    b=build_b(Lx)
    print(A)
    print(b)
    h=optimize(A,b)
    H=build_H(h)
    return(H)
        