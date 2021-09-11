from DmgDistrib import bestbuild
from DmgDistrib import Character
from copy import deepcopy
import csv

a = Character(349,"PJWS",2,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
weapon = ["PJWS","HomaAb","HomaBe","VortexSh","VortexNSh","Spine","Grasscutter"]
header = ['Weapon','flatAtk','ATK%','CritRate%','CritDmg%','ATK','Tot Cr%','Tot Cd%','Damage']
with open ('WeaponsBest.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)    
        for j in range (0,7):
            for i in range(1,6):
                a = Character(349,weapon[j],i,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
                var = bestbuild(a,45)
                writer.writerow(var)
with open ('WeaponsMild.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)    
        for j in range (0,7):
            for i in range(1,6):
                a = Character(349,weapon[j],i,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
                var = bestbuild(a,30)
                writer.writerow(var)            