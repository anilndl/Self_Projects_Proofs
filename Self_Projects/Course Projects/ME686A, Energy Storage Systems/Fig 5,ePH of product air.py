'''                PHYSICAL EXERGY VS TEMPERATURE RATIO AT FOR PRODUCT PRODUCT AIR
                                    DIFFERENT PRESSURE RATIOS'''
import numpy as np
import matplotlib.pyplot as plt
Tr=np.array([1,1.05,1.1,1.15,1.20,1.25])
ePH_1 = np.array([320.75689070515614,
321.46552473697943,
322.64585688201026,
324.7652378054082,
326.88244500478226,
329.9539170506913])
ePH_2 = np.array([382.07547169811323,
382.7841057299365,
383.96226415094344,
386.0859925223894,
388.6792452830189,
391.2724980436484])
ePH_3 = np.array([417.45500391270326,
418.1614642205026,
419.33744891748546,
421.46552473697943,
424.0566037735849,
427.121554647422])
ePH_1= ePH_1-2
ePH_2= ePH_2-2
ePH_3= ePH_3-2
x=[ePH_1,ePH_2,ePH_3]
for i in range(len(x)):
    plt.plot(Tr,x[i], '*-', linewidth =1, markersize = 3)
    print(x[i])
plt.xlabel('Tr')
plt.ylabel('physical exergy of product air')
plt.title(" exergy vs temperature ratio of product air at different pressure ratios")
plt.yticks(np.arange(300,451,50))
plt.legend(['Ph=1','Ph=2','Ph=3'])
plt.show()