from copy import deepcopy
import csv
from typing import Match


class Character:
    def __init__(self,baseATK,weapon,R,flatATK,dATK,CR,CDMG,Edmg,ER) -> None:
        self.baseATK = baseATK
        self.flatATK = flatATK
        self.R = R
        self.dATK = dATK
        self.CR = CR
        self.CDMG = CDMG
        self.Edmg = Edmg
        self.ER = ER
        self.weapon = weapon
       
        match weapon:
            case "PJWS Pre-stacked":
                self.CR = CR + 0.221
                self.baseATK = baseATK + 674
                self.dATK = dATK + 7*(2.5+0.7*R)/100
            case "PJWS Unstacked":
                self.CR = CR + 0.221
                self.baseATK = baseATK + 674
                self.dATK = dATK 
            case "HomaAb":  
                self.CDMG = CDMG + 0.662
                self.baseATK = baseATK + 608
                self.flatATK = flatATK + (12736 * (1+(0.15+0.05*R))+4780)*(0.6+0.2*R)/100
            case "HomaBe":
                self.CDMG = CDMG + 0.662
                self.baseATK = baseATK + 608
                self.flatATK = flatATK + (12736 * (1+(0.15+0.05*R))+4780)*(1.6+0.2*R)/100
            case "VortexSh":
                    self.baseATK = baseATK + 608
                    self.dATK = dATK + 0.496 + (0.03+0.01*R)*5*2
            case "VortexNSh":
                    self.baseATK = baseATK + 608
                    self.dATK = dATK + 0.496 + (0.03+0.01*R)*5
            case "Spine":
                    self.baseATK = baseATK + 674
                    self.CR = CR + (0.06+0.02*R)
            case "Grasscutter":
                    self.baseATK = baseATK + 608
                    self.ER = ER + 0.551
                    self.dATK =  dATK + (ER + 0.551 -1+0.25+0.05*R) * (0.21+0.07*R)
            case "Calamity Queller PreBuffed":
                    self.baseATK = baseATK + 741
                    self.dATK = dATK + 0.165 + (0.024 + 0.008 * R) * 6
                    self.Edmg = Edmg + 0.09 + 0.03 * R
            case "Calamity Queller NoPreBuff":
                    self.baseATK = baseATK + 741
                    self.dATK = dATK + 0.165 
                    self.Edmg = Edmg + 0.09 + 0.03 * R
            case "DM not Solo":
                    self.baseATK = baseATK + 454
                    self.CR  = CR + 0.368
                    self.dATK = dATK + 0.12 + R * 0.04
            case "DM solo":
                    self.baseATK = baseATK + 454
                    self.CR  = CR + 0.368
                    self.dATK = dATK + 0.18 +0.06 *R
            case "Blackcliff 0 Stack":
                    self.baseATK = baseATK + 510
                    self.dATK = dATK + (0.09 +0.03 *R) * 0
                    self.CDMG = CDMG + 0.551
            case "Blackcliff 1 Stack":
                    self.baseATK = baseATK + 510
                    self.dATK = dATK + (0.09 +0.03 *R) * 1
                    self.CDMG = CDMG + 0.551
            case "Blackcliff 2 Stack":
                    self.baseATK = baseATK + 510
                    self.dATK = dATK + (0.09 +0.03 *R) * 2
                    self.CDMG = CDMG + 0.551            
            case "Blackcliff 3 Stack":
                    self.baseATK = baseATK + 510
                    self.dATK = dATK + (0.09 +0.03 *R) * 3
                    self.CDMG = CDMG + 0.551
            case "CrescentPike":
                    self.baseATK = baseATK + 565
            case "Lithic 1 Liyue":
                    self.baseATK = baseATK + 565
                    self.dATK = dATK + 0.276 + (0.06 + R*0.01)
                    self.CR = CR + (0.02 + 0.01 *R)        
            case "Lithic 2 Liyue":
                    self.baseATK = baseATK + 565
                    self.dATK = dATK + 0.276 + (0.06 + R*0.01)*2
                    self.CR = CR + (0.02 + 0.01 *R)*2
            case "Lithic 3 Liyue":
                    self.baseATK = baseATK + 565
                    self.dATK = dATK + 0.276 + (0.06 + R*0.01)*3
                    self.CR = CR + (0.02 + 0.01 *R)*3
            case "Lithic 4 Liyue":
                    self.baseATK = baseATK + 565
                    self.dATK = dATK + 0.276 + (0.06 + R*0.01)*4
                    self.CR = CR + (0.02 + 0.01 *R)*4
            case "The Catch":
                    self.baseATK = baseATK + 510
                    self.ER = ER + 0.459
            case "Starglitter":
                    self.baseATK = baseATK + 510
                    self.ER = ER + 0.459
            case "Kitain Spear":
                    self.baseATK = baseATK+ 565
            case "Dragonspine Spear":
                    self.baseATK = baseATK + 454
            case "Wavebreaker's Fin":
                    self.baseATK = baseATK + 620
                    self.dATK = dATK + 0.138
            case "Royal Spear":
                    self.baseATK = baseATK + 565
                    self.dATK = dATK +0.276
                    #I hate it here
            case "Favonius Lance":
                    self.baseATK = baseATK + 565
                    self.ER = ER + 0.306
            case "Dragonsbane Effect Off":
                    self.baseATK = baseATK + 454
            case "Dragonsbane Effect On":
                    self.baseATK = baseATK + 454
                    self.Edmg = Edmg + 0.16 + 0.04 * R
            case "White Tassel":
                    self.baseATK = baseATK + 401
                    self.CR = CR + 0.234
            case "Black Tassel":
                    self.baseATK = baseATK + 354
            case "Halberd":
                    self.baseATK = baseATK + 448
                    self.dATK = dATK + 0.234


    def substat(self,flatATK,dATK,CR,CDMG) -> None:
        self.dATK = self.dATK + dATK * 5.8/100
        self.flatATK = self.flatATK + flatATK * 19
        self.CR = self.CR + CR * 3.9/100
        self.CDMG = self.CDMG + CDMG * 7.8/100

    def rawDMG(self,talent,Bdmg,res,resShred,charlvl,enemylvl,defShred, Average):
        a1 = charlvl + 100
        a2 = enemylvl +100
        defMiti = a1/(a1+a2*(1-defShred))
        if (res - resShred) < 0:
            resMiti = 1 + (resShred - res)/2
        else:
            resMiti = 1 - res + resShred
        aux1 =  defMiti * resMiti * talent
        if Average:
            CritMulti = (1+self.CDMG*self.CR)
        else:
            CritMulti = (1+self.CDMG)

        offmulti = (self.baseATK * (1 + self.dATK)+ self.flatATK) * CritMulti * (1+self.Edmg+ Bdmg)
        
        return  offmulti * aux1

    def PerfectRotation(self,Bdmg,res,resShred,charlvl,enemylvl,defShred,Average,ttds,bennet):
        a1 = charlvl + 100
        a2 = enemylvl +100
        defMiti = a1/(a1+a2*(1-defShred))
        if (res - resShred) < 0:
            resMiti = 1 + (resShred - res)/2
        else:
            resMiti = 1 - res + resShred
        aux1 =  defMiti * resMiti 
        if Average:
            if self.CR >=1:
                CritMulti = (1+self.CDMG)
            else:
                CritMulti = (1+self.CDMG*self.CR)
        else:
            CritMulti = (1+self.CDMG)
            
        if bennet == 1 and self.weapon=="HomaBe":    
            offmulti1 =(self.baseATK * (1 + self.dATK)+ self.flatATK)- (12736 * (1+(0.15+0.05*self.R))+4780)*(1)/100
        else:
            offmulti1 =(self.baseATK * (1 + self.dATK)+ self.flatATK)
        hp = 4.0402
        e = 4.5504
        as1 = [0.05, 0.1, 0.15, 0.15,0.2, 0.2,0.25]
        acount = [2, 3 , 1, 1, 2 ,1, 2]
        buff10 = [1, 1 , 1, 1, 0 ,0, 0]
        buff12 = [1, 1 , 1, 1, 1 ,0, 0]
        CalamityBuff = (0.024 + 0.008 * self.R)
        rotation1=0        
        if self.weapon == "PJWS Pre-stacked":
                bonus = (1+self.Edmg+Bdmg+((self.R)*3+9)/100)
        else:
                bonus = (1+self.Edmg+Bdmg)

        for i  in range (0,7):
            if self.weapon == "Calamity Queller NoPreBuff":
                if i == 0:
                    rotation1 += hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*CalamityBuff*3)
                    rotation1 += hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*CalamityBuff*4)
                elif i == 1:
                    rotation1 += hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*CalamityBuff*5)
                    rotation1 += 2*hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*CalamityBuff*6)
                else:
                    rotation1 += acount[i]*hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*CalamityBuff*6)
            elif self.weapon == "PJWS Unstacked":
                if i == 0:
                    rotation1 += hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*(2.5+0.7*self.R)/100*2)
                    rotation1 += hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*(2.5+0.7*self.R)/100*3)
                elif i == 1:
                    rotation1 += hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*(2.5+0.7*self.R)/100*4)
                    rotation1 += hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*(2.5+0.7*self.R)/100*5)
                    rotation1 += hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*(2.5+0.7*self.R)/100*6)
                else:
                    rotation1 += acount[i]*hp*(bonus+as1[i]+(self.R*3+9)/100)*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet+self.baseATK*(2.5+0.7*self.R)/100*7)
            else:
                rotation1 += acount[i]*hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet)

        if self.weapon == "Kitain Spear":
            rotation1 += (e * 2 * (bonus-0.952+0.045+0.015*self.R))*offmulti1+(e * 2 * (bonus-0.952+0.045+0.015*self.R))*(offmulti1+ttds*0.48*self.baseATK+1202*bennet)
        else:
            if self.weapon == "PJWS Unstacked":
                rotation1 += (e * 2 * (bonus-0.952))*offmulti1+(e * 2 * (bonus-0.952+(self.R*3+9)/100)*(offmulti1+ttds*0.48*self.baseATK+1202*bennet))
            else:
                rotation1 += (e * 2 * (bonus-0.952))*offmulti1+(e * 2 * (bonus-0.952))*(offmulti1+ttds*0.48*self.baseATK+1202*bennet)
        if (self.weapon == "Lithic 4 Liyue") and bennet:
            #Come on, bennet is not from liyue
            return 0
        else:
            return  aux1 * rotation1 *CritMulti

   

def bestbuild(a,submax,cratecap,bennet,ttds):
    aux = 0
    holder= []
    index = 0
    max = 0
    maxi = 0
    flex = 0
    flexM = 0
    header = ['index','flatAtk','ATK%','CritRate%','CritDmg%','Damage']
    with open ('data.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        for i in range(0,31):
            for j in range (0,31):
                for k in range (0,31):
                    for l in range (0,31):
                        if (i+j+k+l)==submax:
                            if not((i>24) or (j>24) or (k>24) or (l>30)):
                                if not((i>24) or (j>24) or (k>24) or (l>30)):
                                    flexCounter = 0
                                    if i>4:
                                        flexCounter += (i-4)
                                    if j>4:
                                        flexCounter += (j-4)
                                    if k>4:
                                        flexCounter += (k-4)
                                    if l>4:
                                        flexCounter += (l-5)
                                    if flexCounter <= 25:
                                        if (a.CR+(k-1)*3.9/100)<=1:
                                                y = deepcopy(a)
                                                y.substat(i,j,k,l)
                                                if y.CR <= cratecap+3.9/100:
                                                    b1 = y.PerfectRotation(0.952,0.1,0,90,90,0,1,ttds,bennet)
                                                    if b1 > max:
                                                        max = b1
                                                        maxi = index
                                                                
                                                    b2 = [index, i, j, k, l]
                                                    writer.writerow([index, i, j, k, l,b1])
                                                    
                                                    index += 1
                                                    holder.append([b2,b1])         
                                else:
                                    break               
    print("-----------------------------------------------")
    #print(holder)
    print("Best build of substats for single high plunge is: ")
    print("Build N°:",maxi," Which has the following sub count:")
    e=holder[:][maxi]
    print("Flat ATK:", e[0][1])
    print("ATK%:", e[0][2])
    print("Flat Crit Rate%:", e[0][3])
    print("Flat Crit Dmg%:", e[0][4])
    print("Dealing this amount of damage:", e[:][1])
    a.substat(e[0][1],e[0][2],e[0][3],e[0][4])
    print("Stats: ",(a.baseATK*(a.dATK+1))+a.flatATK,"ATK")
    print("CR",a.CR*100)
    print("cdmg",(a.CDMG*100))
    if (bennet or ttds):    
        var = [a.weapon+" R"+str(a.R) , e[0][1],e[0][2],e[0][3],e[0][4],(a.baseATK*(a.dATK+1))+a.flatATK,(a.baseATK*(a.dATK+1))+a.flatATK+bennet*1207+ttds*0.48*a.baseATK,a.CR,a.CDMG,max]
    else:
        var = [a.weapon+" R"+str(a.R) , e[0][1],e[0][2],e[0][3],e[0][4],(a.baseATK*(a.dATK+1))+a.flatATK,a.CR,a.CDMG,max]
    return var