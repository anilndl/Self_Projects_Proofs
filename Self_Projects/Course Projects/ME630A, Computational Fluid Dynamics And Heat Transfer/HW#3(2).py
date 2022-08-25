'''                                                             PAPPU ANIL KUMAR
                                                                        21105059                                 '''

import numpy as np
import math
import matplotlib.pyplot as plt
'''                               INITIALISING GRID AND INITIAL VALUES                    '''

npx = 200
npy = 10
Ra=[500,3000]
Pr=7
crf=1
x=np.linspace(0,20,npx+1)                                 # DEFINE X
y=np.linspace(0,1,npy+1)                             # DEFINE Y
u=np.zeros((npx+1,npy+1),dtype=float)                                 # INITILISING  U
v=np.zeros((npx+1,npy+1),dtype=float)                                 # INITIALISING V
pi =np.zeros((npx+1,npy+1),dtype=float)                             # INITIALISING STREAM FUNCTION
w = np.zeros((npx+1,npy+1),dtype=float)                             # INITIALISING VORTICITY
T = np.zeros((npx+1,npy+1),dtype=float)                             # INITIALISING THETA
itr=1
dx=x[1]-x[0]
dy=y[1]-y[0]

print(dx,'\t',dy)
for k in Ra:
    rms=1
    while rms>=10**(-5):
        rms = 0
        #BOTTOM FACE(Y=0)
        pi[:, 0] = 0
        w[:, 0] = 2 * (pi[:, 0] - pi[:, 1]) / dy ** 2
        T[:, 0] = 1
        # LEFT FACE(X=0)
        pi[0, 1:npy] = 0
        w[0, 1:npy] = 2 * (pi[0, 1:npy] - pi[1, 1:npy]) / dx ** 2
        T[0, 1:npy] = (4 * T[1, 1:npy] - T[2, 1:npy]) / 3
        # TOP PLATE(Y =L)
        pi[:, npy] = 0
        w[:, npy] = 2 * (pi[:, npy] - pi[:, npy - 1]) / dy ** 2
        T[:, npy] = 0
        # RIGHT PLATE(X=20L)
        pi[npx, 1:npy] = 0
        w[npx, 1:npy] = 2 * (pi[npx, 1:npy] - pi[npx - 1, 1:npy]) / dx ** 2
        T[npx, 1:npy] = (4 * T[npx - 1, 1:npy] - T[npx - 2, 1:npy]) / 3

        '''                 INTERIOR POINTS             '''
        for i in range(1,npx):
            for j in range(1,npy):

                '''             w                    '''
                z=2*Pr/dx
                a=-u[i-1,j]-2*Pr/dx
                b=4*Pr*2/dx
                c=u[i+1,j]-2*Pr/dx
                d=-v[i,j-1]-2*Pr/dx
                e=v[i,j+1]-2*Pr/dx
                s=k*Pr*(T[i+1,j]-T[i-1,j])
                res=s-w[i-1,j]*a-c*w[i+1,j]-d*w[i,j-1]-e*w[i,j+1]-b*w[i,j]
                w[i,j]=w[i,j]+crf*res/b
                rms=rms+res*res
                '''         pi                      '''
                res=-w[i,j]*dx**2-(pi[i+1,j]+pi[i-1,j]-4*pi[i,j]+pi[i,j-1]+pi[i,j+1])
                pi[i,j]=pi[i,j]+crf*res/(-4)
                rms=rms+res*res

                '''         T                   '''
                a=-u[i-1,j]-2/dx
                b=4*2/dx
                c=u[i+1,j]-2/dx
                d=-v[i,j-1]-2/dx
                e=v[i,j+1]-2/dx
                res=0-a*T[i-1,j]-b*T[i,j]-c*T[i+1,j]-d*T[i,j-1]-e*T[i,j+1]
                T[i,j]=T[i,j]+crf*res/(b)
                rms=rms+res*res
                res=(pi[i,j+1]-pi[i,j-1])*0.5/dx-u[i,j]
                u[i,j]=u[i,j]+crf*res/1
                rms=rms+res*res
                res=(pi[i-1,j]-pi[i+1,j])*0.5/dx-v[i,j]
                v[i,j]=v[i,j]+res*crf/1
                rms=rms+res*res
        rms=math.sqrt(rms)
        itr=itr+1
        print(itr,'\t\t', rms)
    # TEMPERATURE PLOT
    Tnew=T.transpose()
    X,Y=np.meshgrid(x,y)
    plt.contourf(X,Y,Tnew)
    plt.colorbar()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("contour of theta")
    plt.show()
    # STREAM FUNCTION PLOT
    pinew = pi.transpose()
    X,Y = np.meshgrid(x,y)
    plt.contourf(X,Y,pinew)
    plt.colorbar()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("contour of stream function")
    plt.show()
    # vorticity function
    wnew = w.transpose()
    X,Y = np.meshgrid(x,y)
    plt.contourf(X,Y,wnew)
    plt.colorbar()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("contour of vorticity function")
    plt.show()
    plt.plot(y,u[100,:])
    plt.xlabel("X")
    plt.ylabel('U')
    plt.title("velocity curv at x=10L")
    plt.show()
    plt.plot(x,u[:,5])
    plt.xlabel("X")
    plt.ylabel('U')
    plt.title("velocity curve at y=L/2")
    plt.show()
    plt.plot(y,T[100,:])
    plt.xlabel("y")
    plt.ylabel('theta')
    plt.title("Temperature curve at x=10L")
    plt.show()
    plt.plot(x,T[:,5])
    plt.xlabel("x")
    plt.ylabel('theta')
    plt.title("temperature curve at y=L/2")
    plt.show()











