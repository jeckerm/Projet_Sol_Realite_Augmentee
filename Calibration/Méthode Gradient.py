import numpy as np

#def gradient(M):

A= np.matrix([[1],[1],[0],[1],[0],[0],[1],[0],[1],[1],[1],[1]])
print(A)
print(int(A[3][0]))


def norme_vecteur(X):
    n=len(X)
    S=0
    for i in range(0,n):
        S+=int(X[i][0])*int(X[i][0])
    return(S)

def produit_scalaire_vecteurs(X,Y,A="Vide"):
    n = len(X)
    if A=="Vide":
        A=np.eye(n,n)
    p = len(Y)
    m = len(A)
    o = np.size(A)/len(A)
    if n!=p or p!=m or m!=o:
        print ("Produit scalaire avec deux vecteurs de dimensions différentes ou une matice de dimension inadaptée")
        return(0)
    else:
        X=A*X
        S=0
        for i in range(0,n):
            S+= int(X[i][0])*int(Y[i][0])
        return(S)


def gradient(A,b, x0,eps0, eps1, kmax):
    r = A*x0-b
    diff_normes_x = eps0+1
    k = 0
    x = x0
    while (diff_normes_x>eps0) and k<=kmax and norme_vecteur(r)>eps1:
        if k == 0:
            d = r
        else:
            alpha = - (produit_scalaire_vecteurs(r,d,A))/(produit_scalaire_vecteurs(d,d,A))
            d = r + alpha*d
        rho = - (produit_scalaire_vecteurs(r,d,A))/(produit_scalaire_vecteurs(d,d,A))
        x0 = x0 + rho*d
        r= A*x0 - b
        k = k + 1
    return(x0)