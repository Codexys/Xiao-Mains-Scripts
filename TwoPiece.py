from DmgDistrib import bestbuild
from DmgDistrib import Character
from copy import deepcopy
import csv
import os
folderpth = str(os.path.realpath(os.getcwd())) + '\Results\TwoPiece'
if not os.path.exists(folderpth):
    os.mkdir(folderpth)

#Parameters
bennet = 0
ttds = 0
cratecap = 1
#Stats
a = Character(349,"PJWS",2,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
#Array shenanigans
weapon = ["PJWS","HomaAb","HomaBe","VortexSh","VortexNSh","Spine","Grasscutter","DM not Solo","DM solo","Blackcliff 0 Stack", "Blackcliff 1 Stack", "Blackcliff 2 Stack","Blackcliff 3 Stack","CrescentPike","Lithic 1 Liyue","Lithic 2 Liyue","Lithic 3 Liyue","Lithic 4 Liyue","The Catch","Starglitter","Kitain Spear","Dragonspine Spear","Royal Spear","Favonius Lance","Dragonsbane Effect Off","Dragonsbane Effect On","White Tassel","Black Tassel","Halberd"]

rolls = [20, 25 , 30, 35, 40, 42]
bennetBuff = [0, 0, 1, 1]
ttdsBuff =   [0, 1, 0, 1]
textBuff = ["Solo","TTDS","Bennet","Bennet&TTDS"]
Res = ['','PyroRes','GeoRes']

for q in range (len(Res)):
    for l in range(len(bennetBuff)):
        for k in range (len(rolls)):
                filepth = folderpth + '\Shime&VV'+ Res[q] +str(rolls[k])+'Subs'+textBuff[l]+'.csv'
                with open (filepth,'w',encoding='UTF8',newline='') as f:
                        writer=csv.writer(f)
                        if l > 0:
                                header = ['Weapon','flatAtk','ATK%','CritRate%','CritDmg%','Total Atk Pre Buff',"Total Atk Post Buff",'Tot Cr%','Tot Cd%','Damage']
                        else:    
                                header = ['Weapon','flatAtk','ATK%','CritRate%','CritDmg%','ATK','Tot Cr%','Tot Cd%','Damage']
                        writer.writerow(header+header)
                        bennet = bennetBuff[l]
                        ttds = ttdsBuff[l]    
                        for j in range (len(weapon)):
                            for i in range(1,6):
                                Viri = Character(349,weapon[j],i,311,0.466+0.18+0.25, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
                                var1 = bestbuild(Viri,rolls[k],cratecap,bennet,ttds)
                                Shime = Character(349,weapon[j],i,311,0.466+0.18*2+0.25, 0.242 , 0.5+0.622 , 0.466 , 1+6.48/100*3 )
                                var2 = bestbuild(Shime,rolls[k],cratecap,bennet,ttds)
                                var1[0]='Viri '+var1[0]
                                var2[0]='Shime '+var2[0]
                                if var2[len(var2)-1] == 0:
                                    var2[len(var2)-1] = 1
                                diff = var1[len(var1)-1]/var2[len(var2)-1]-1
                                if diff < 0:
                                    if var1[len(var1)-1] == 0:
                                        var1[len(var1)-1] = 1
                                    diff = var2[len(var2)-1]/var1[len(var1)-1]-1
                                    winner = "Shime"
                                else:
                                    winner = "Viri"
                                result = [diff,winner]
                                writer.writerow(var1+var2+result)
                            
                    