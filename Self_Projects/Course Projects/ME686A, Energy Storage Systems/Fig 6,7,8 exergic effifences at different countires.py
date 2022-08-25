'''                           EXEGERTC EFFICIENCY OF FUEL CELL AT DIFFERENT PRESSURE RATIOS
                                            BY VARYING TEMPERATURE RATIOS AT 0.5V
                                                            FIG-6'''

import numpy as np
import matplotlib.pyplot as plt
Tr=[1,1.05,1.1,1.15,1.20,1.25]
''' AT 1 atm pressure '''
m_r_air=0.02142
m_H2 = 0.00021
m_water = 0.001868
m_p_air = 0.019762
W=10
# exergy of reactants = exergy of incoming air + H2
ePH_r_H2= np.array(((0.0, 5.155594408382487, 19.985199781850103, 43.628458762498774, 75.33491787824184, 114.44607042962676),
                    (843.9363986394716, 849.0919930478541, 863.9215984213217, 887.5648574019704, 919.2713165177134, 958.3824690690984),
                    (1337.6075448372242, 1342.7631392456065, 1357.5927446190742, 1381.2360035997228, 1412.9424627154658, 1452.0536152668508)))
ePH_r_air = np.array(([0.0, 0.36233373289681103, 1.4045542504027517, 3.066195878063724, 5.294516955778533, 8.043237816907332],
                      [59.31161403025656, 59.673947763153365, 60.7161682806593, 62.37780990832028, 64.60613098603508, 67.35485184716389],
                      [94.00668409520348, 94.3690178281003, 95.41123834560624, 97.0728799732672, 99.30120105098202, 102.04992191211082]))
EPH_r_air = m_r_air*ePH_r_air
ECH_r_air = 0
EPH_r_H2 = ePH_r_H2*m_H2
ECH_r_H2 = 159138*m_H2
Er = EPH_r_H2 + EPH_r_air + ECH_r_air + ECH_r_H2
ePH_p_air = np.array(([320.75689070515614,
321.46552473697943,
322.64585688201026,
324.7652378054082,
326.88244500478226,
329.9539170506913],
[382.07547169811323,
382.7841057299365,
383.96226415094344,
386.0859925223894,
388.6792452830189,
391.2724980436484],
[417.45500391270326,
418.1614642205026,
419.33744891748546,
421.46552473697943,
424.0566037735849,
427.121554647422]))
ePH_p_water= np.array(([0,
99.5634272658027,
199.92,
298.788,
398.4,
497.9893373952779],
[81.62985529322145,
180.42,
279.12,
378,
476.8,
575.5521706016755],
[161.23381568926118,
260,
358.79,
457.55,
556.34,
655.11]))
EPH_p_air= m_p_air*ePH_p_air
ECH_p_air = 8.58*0.019762
EPH_p_water = ePH_p_water*0.001868
ECH_p_water = 2.5*0.001868
Ep = EPH_p_air+EPH_p_water+ECH_p_air+ECH_p_air
Enet = Er-Ep
print(Ep)
print(Er)
print(Enet)
for i in range(3):
    n=[]
    for j in range(6):
        e = W/Enet[i,j]
        e = e*100
        n.append(e)
    print('n = ',n)
    plt.plot(Tr,n,'*-',linewidth=1,markersize = 3)
plt.xlabel("Tr")
plt.ylabel('efficiency')
plt.yticks(np.arange(37.1,39,0.1))
plt.title("efficiency vs Temperature ratios at different pressures, 0.5V")
plt.legend(["Pr=1",'Pr=2', 'Pr=3'])
print("firstgraph\n")
plt.show()



'''                                                             EXERGETIC EFFICIENCY AT OPERATING FUEL CELL
                                                                    VOTAGE V = 0.5V AND 0.6V AND Pr = 1
                                                                            FIG 7.'''

m_r_air=[0.02142,0.01785]
m_r_H2 = [0.00021,0.000175]
m_p_water = [0.001868,0.001557]
m_p_air = [0.019762,0.01647]
for i in range(2):
    n=np.zeros(6)
    ECH_r_air=0
    ECH_r_H2 = 159138*m_r_H2[i]
    EPH_r_air = m_r_air[i]*ePH_r_air[0]
    EPH_r_H2 = m_r_H2[i]*ePH_r_H2[0]
    Er = EPH_r_air+ EPH_r_H2 + ECH_r_air+ ECH_r_H2
    EPH_p_air = ePH_p_air[0]*m_p_air[i]
    EPH_p_water = ePH_p_water[0]*m_p_water[i]
    ECH_p_air = 8.58*m_p_air[i]
    ECH_p_water = 2.5*m_p_water[i]
    Ep = EPH_p_air + EPH_p_water + ECH_p_air + ECH_p_water
    n = W/(Er-Ep)
    n = n*100
    print('n =',n)
    plt.plot(Tr,n,"*-", linewidth=1,markersize =3)
plt.yticks(np.arange(35,51,5))
plt.xlabel("Tr")
plt.ylabel('efficiency')
plt.title("efficiency vs Temperature ratios at different voltages, Pr =1")
plt.legend(["V =0.5v",'V=0.6v'])
print("second graph\n")
plt.show()




'''                                      EXERGETIC EFFICIENCY AT VARIABLE STIOCHIOMETRIC RATIOS
                                                   V = 0.5V AND Pr = 1
                                                        FIG 8'''
m_r_air = [0.0148,0.02142,0.02556]
m_H2 = 0.00021
m_water = 0.001868
m_p_air = [0.0126,0.019762,0.0269]
for i in range(3):
        EPH_r_air = m_r_air[i] * ePH_r_air[0]
        ECH_r_air = 0
        EPH_r_H2 = ePH_r_H2[0] * m_H2
        ECH_r_H2 = 159138 * m_H2
        Er = EPH_r_H2 + EPH_r_air + ECH_r_air + ECH_r_H2
        EPH_p_air = m_p_air[i] * ePH_p_air[0]
        ECH_p_air = 8.58 * m_p_air[i]
        EPH_p_water = ePH_p_water[0] * 0.001868
        ECH_p_water = 2.5 * 0.001868
        Ep = EPH_p_air + EPH_p_water + ECH_p_air + ECH_p_air
        Enet = Er - Ep
        n = W/Enet
        n = n*100
        print(n)
        plt.plot(Tr,n,'*-',linewidth=1,markersize=3)
        plt.yticks(np.arange(30,46,5))
        plt.xticks(np.arange(1,1.26,0.05))
plt.xlabel("T/To")
plt.ylabel('Efficiency(%)')
plt.legend(['λ = 2','λ = 3','λ = 4'])
plt.title( 'EXERGETIC EFFICIENCY AT VARIABLE STIOCHIOMETRIC RATIOS')
print("third graph\n")
plt.show()



