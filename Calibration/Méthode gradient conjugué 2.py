import numpy as np

#def gradient(M):

A= np.matrix([[1],[1],[0],[1],[0],[0],[1],[0],[1],[1],[1],[1]])
print(A)
print(int(A[3][0]))


def norme_vecteur(X):
    return((np.transpose(X)*X)[0,0])

def produit_scalaire_vecteurs(X,Y,A="Vide"):
    n = len(X)
    if A=="Vide":
        A=np.matrix(np.eye(n,n))
    p = len(Y)
    m = len(A)
    o = np.size(A)/len(A)
    if n!=p or p!=m or m!=o:
        print ("Produit scalaire avec deux vecteurs de dimensions différentes ou une matice de dimension inadaptée")
        return(0)
    else:
        return(((np.transpose(X))*A*Y)[0,0])

def gradient(A,b, x0,eps0, eps1, kmax):
    r = b-A*x0
    #print(A)
    #print(x0)
    #print(b)
    #print(A*x0)
    #print("abcd")
    r0=r
    #print("r: ",r)
    diff_normes_x = eps0+1
    k = 0
    rho=r
    x = x0
    while (diff_normes_x>eps0) and k<=kmax and norme_vecteur(r)>eps1:
        #print(k)
        alpha = - (norme_vecteur(r))/(produit_scalaire_vecteurs(rho,rho,A))
        x0 = x
        x = x + alpha*rho
        diff_normes_x= norme_vecteur(x-x0)
        r0=r
        r=r-alpha*A*rho
        beta = norme_vecteur(r)/norme_vecteur(r0)
        rho = r + beta*rho
        #print("d", d)
        #print("Produit scalaire:", produit_scalaire_vecteurs(d,d,A))
        #print(x0 , x)
        k = k + 1
        #print(x-x0)
    return(x, k,diff_normes_x)