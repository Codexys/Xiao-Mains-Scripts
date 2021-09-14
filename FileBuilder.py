from DmgDistrib import bestbuild
from DmgDistrib import Character
from copy import deepcopy
import csv
#Parameters
bennet = 1
ttds = 0
cratecap = 1
#Stats
a = Character(349,"PJWS",2,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
#Array shenanigans
weapon = ["PJWS","HomaAb","HomaBe","VortexSh","VortexNSh","Spine","Grasscutter","DM not Solo","DM solo","Blackcliff 0 Stack", "Blackcliff 1 Stack", "Blackcliff 2 Stack","Blackcliff 3 Stack","CrescentPike","Lithic 1 Liyue","Lithic 2 Liyue","Lithic 3 Liyue","Lithic 4 Liyue","The Catch","Starglitter","Kitain Spear","Dragonspine Spear","Royal Spear","Favonius Lance","Dragonsbane Effect Off","Dragonsbane Effect On","White Tassel","Black Tassel","Halberd"]
if bennet or ttds:
    header = ['Weapon','flatAtk','ATK%','CritRate%','CritDmg%','Total Atk Pre Buff',"Total Atk Post Buff",'Tot Cr%','Tot Cd%','Damage']
else:    
    header = ['Weapon','flatAtk','ATK%','CritRate%','CritDmg%','ATK','Tot Cr%','Tot Cd%','Damage']

with open ('Weapons45Subs.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)    
        for j in range (len(weapon)):
            for i in range(1,6):
                a = Character(349,weapon[j],i,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
                var = bestbuild(a,45,cratecap,bennet,ttds)
                writer.writerow(var)
with open ('Weapons35Subs.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)    
        for j in range (len(weapon)):
            for i in range(1,6):
                a = Character(349,weapon[j],i,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
                var = bestbuild(a,35,cratecap,bennet,ttds)
                writer.writerow(var)            
with open ('Weapons30Subs.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)    
        for j in range (len(weapon)):
            for i in range(1,6):
                a = Character(349,weapon[j],i,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
                var = bestbuild(a,30,cratecap,bennet,ttds)
                writer.writerow(var)            
with open ('Weapons25Subs.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)    
        for j in range (len(weapon)):
            for i in range(1,6):
                a = Character(349,weapon[j],i,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
                var = bestbuild(a,25,cratecap,bennet,ttds)
                writer.writerow(var)                  
with open ('Weapons20.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)    
        for j in range (len(weapon)):
            for i in range(1,6):
                a = Character(349,weapon[j],i,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
                var = bestbuild(a,20,cratecap,bennet,ttds)
                writer.writerow(var)
        