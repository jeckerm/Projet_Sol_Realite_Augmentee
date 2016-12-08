import scipy
import numpy as np
from numpy import *
from tkinter import *

#def demande_de_valeurs():
#Jacobi([[1],[1],[0],[1],[0],[0],[1],[0],[1],[1],[1],[1]],[[1],[0],[1],[3],[2],[9],[3],[9],[3],[4],[0],[4]],[[1,2,3,1,0,0,0,0,0,0,0,0],[5,6,9,1,0,0,0,0,0,0,0,0],[1,2,3,1,0,0,0,0,0,0,0,0],[4,5,3,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,2,3,1,0,0,0,0],[0,0,0,0,5,6,9,1,0,0,0,0],[0,0,0,0,1,2,3,1,0,0,0,0],[0,0,0,0,4,5,3,1,0,0,0,0],[0,0,0,0,0,0,0,0,1,2,3,1],[0,0,0,0,0,0,0,0,5,6,9,1],[0,0,0,0,0,0,0,0,4,5,3,1],[0,0,0,0,0,0,0,0,1,2,3,1]])

"""A= matrix([[1],[1],[0],[1],[0],[0],[1],[0],[1],[1],[1],[1]])
B= matrix([[1,2,3,1,0,0,0,0,0,0,0,0],[5,6,9,1,0,0,0,0,0,0,0,0],[1,2,3,1,0,0,0,0,0,0,0,0],[4,5,3,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,2,3,1,0,0,0,0],[0,0,0,0,5,6,9,1,0,0,0,0],[0,0,0,0,1,2,3,1,0,0,0,0],[0,0,0,0,4,5,3,1,0,0,0,0],[0,0,0,0,0,0,0,0,1,2,3,1],[0,0,0,0,0,0,0,0,5,6,9,1],[0,0,0,0,0,0,0,0,1,2,3,1],[0,0,0,0,0,0,0,0,4,5,3,1]])
C = B*A """

#Jacobi([[1.1],[0.9],[0.1],[1.1],[-0.1],[0.1],[1.1],[0.1],[0.9],[1.1],[0.9],[0.9]],[[4],[12],[4],[10],[3],[9],[3],[3],[7],[21],[7],[13]],[[1,2,3,1,0,0,0,0,0,0,0,0],[5,6,9,1,0,0,0,0,0,0,0,0],[1,2,3,1,0,0,0,0,0,0,0,0],[4,5,3,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,2,3,1,0,0,0,0],[0,0,0,0,5,6,9,1,0,0,0,0],[0,0,0,0,1,2,3,1,0,0,0,0],[0,0,0,0,4,5,3,1,0,0,0,0],[0,0,0,0,0,0,0,0,1,2,3,1],[0,0,0,0,0,0,0,0,5,6,9,1],[0,0,0,0,0,0,0,0,4,5,3,1],[0,0,0,0,0,0,0,0,1,2,3,1]])

#Jacobi([[1],[1],[0],[1],[0],[0],[1],[0],[1],[1],[1],[1]],[[1],[0],[1],[3],[2],[9],[3],[9],[3],[4],[0],[4]],[[1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,1]])    

def Jacobi(X0, b, A):
    
    #Warning 1: on prendra n = 4 ici!
    
    #Soit n le nombre de mesures effectuées.
    #A est une matrice de taille 3n*12, diagonale par bloc (3 blocs de taille n*4), contenant les données mesurées
    #b est un vecteur de taille 3n contenant la position des points envoyés par le vidéo projecteur
    #X est un vecteur de taille 12. Ces coefficients correspondent aux coefficient de l'homographie lue lignes par lignes
    
    #Warning: X1, Y2 et Z3 doivent être non nuls... Sinon, D n'est pas inversible
    if (A[0][0] == 0) or (A[1][1] == 0) or (A[2][2] == 0):
        print("X1, Y1 ou Z1 est nul. Ceci rend D non inversible. Veuillez procéder à une nouvelle mesure")
        return("X1, Y1 ou Z1 est nul. Ceci rend D non inversible. Veuillez procéder à une nouvelle mesure")
    
    #Initialisation:
    n = len(b)/3
    print(n)
    
    if n!=4:
        print("Cette version n'est pas apte à prendre une série ne contenant pas exactement 4 mesures")
        return("X1, Y1 ou Z1 est nul. Ceci rend D non inversible. Veuillez procéder à une nouvelle mesure")
    
    """D= np.eye(3*n,12)
    for i in range(0,n):
        D[i][i] = A[i][i]
    
    #On construit l'inverse de D: C
    C= np.eye(3*n,12)
    for i in range(0,n):
        C[i][i] = 1/A[i][i]
    
    E= zero([n,n])
    for i in range(1,n):
        for j in range(0,i-1):
            E[i,j]=-A[i][j]
    
    F= zero([n,n])
    for i in range(1,n):
        for j in range(i,n):
            F[i,j]=-A[i][j]"""
    
    #On cherhce à rendre le rayon spectral de A plus petit que 1.
    
    #On cherche le rayon spectral de A
    max=0
    for i in range (0,3):
        m=A[i][i]
        if abs(m)>max:
            max=abs(m)
    
    #On divise les coefficients de A et ceux de b par max + 1
    """for i in range (0,12):
        b[i][0]=b[i][0]/(max+1)
        for j in range (0,12):
            A[i][j]=A[i][j]/(max+1)"""
    
    print(matrix(A))
    
    L=[X0]
    
    
    k=0
    while k<100:
        X=zeros([12,1])
        for i in range (0,12):
            x=0
            for p in range (0,12):
                if p!=i:
                    x+= -(A[i][p]*L[k][p][0])/A[i][i]
            x+=b[i][0]/A[i][i]
            X[i][0]=x
        L.append(X)
        k+=1
    MatA=matrix(A)
    Matb=matrix(b)
    MatX=matrix(X)
    r=MatA*MatX-Matb
    return(X,r)
    