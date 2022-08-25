'''                PHYSICAL EXERGY VS TEMPERATURE RATIO AT FOR PRODUCT WATER
                                    DIFFERENT PRESSURE RATIOS'''
import numpy as np
import matplotlib.pyplot as plt
To = 298    #general assumption
Cp = 4.18
k = 1
Pressure=[1,2,3]  # in atm
T=np.array([25,40,55,70,85,100])
Tr=np.array([1,1.05,1.1,1.15,1.20,1.25])
''' EXERGY VALUES OF WATER ARE OBTAINED FROM PLOT SOFTWARE'''
#    THESE VALUES ARE OBTAINED FROM LINEAR INTERPOLATION.
#    ePH_1 = 1991.2(Tr-1
#    ePH_2 = 1975.92(Tr-1) + 81.62
#    ePH_3 = 1975.52(Tr-1) + 161.23
ePH_3= np.array([161.23381568926118,
260,
358.79,
457.55,
556.34,
655.11])
ePH_2=np.array([81.62985529322145,
180.42,
279.12,
378,
476.8,
575.5521706016755])
ePH_1 = np.array([0,
99.5634272658027,
199.92,
298.788,
398.4,
497.9893373952779])
for  x in [ePH_1,ePH_2,ePH_3]:
    plt.plot(Tr,x, "*-", linewidth=1, markersize=3)
plt.xlabel('Temperature ratio')
plt.ylabel('Exergy of water')
plt.yticks(np.arange(0,801,200))
plt.legend(["Ph =1",'Ph=2','Ph=3'])
plt.title('Exergy of water vs Temperature ratio at different preesure ratios')
plt.show()