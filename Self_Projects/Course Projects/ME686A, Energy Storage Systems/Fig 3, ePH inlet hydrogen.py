'''                PHYSICAL EXERGY VS TEMPERATURE RATIO AT FOR HYDROGEN
                                    DIFFERENT PRESSURE RATIOS'''
import numpy as np
import matplotlib.pyplot as plt
To = 298    #general assumption
Cp = 14.3
k = 1.4
Pr=[1,2,3]
Tr=np.arange(1,1.26,0.05)
ePH=[]
for j in Pr:
    for i in Tr:
        a=np.log(i)
        b=np.log((j**(0.4/1.4)))
        x=Cp*To*(i-1-a+b)
        ePH.append(x)
    plt.plot(Tr,ePH,'*-', markersize=3,linewidth=1)
    print(ePH)
    ePH=[]
plt.xlabel("T/To")
plt.ylabel("Physical exergy of air(Kj/kg)")
plt.legend(['Pr=1','Pr=2','Pr=3'])
plt.title("physical exergy of inlet Hydrogen")
plt.yticks(np.arange(0,1601,400))
plt.xticks(np.arange(1,1.26,0.05))
plt.show()
