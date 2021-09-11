from copy import deepcopy
import csv


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
        if weapon == "PJWS":
            self.CR = CR + 0.221
            self.baseATK = baseATK + 674
            self.dATK = dATK + 7*(2.5+0.7*R)/100
        elif weapon == "HomaAb" or weapon == "HomaBe":
            self.CDMG = CDMG + 0.662
            self.baseATK = baseATK + 608
            if weapon == "HomaAb":
                self.flatATK = flatATK + (12736 * (1+(0.15+0.05*R))+4780)*(0.6+0.2*R)/100
            else:
                self.flatATK = flatATK + (12736 * (1+(0.15+0.05*R))+4780)*(1.6+0.2*R)/100
        elif weapon == "VortexSh" or weapon == "VortexNSh":
                self.baseATK = baseATK + 608
                if weapon == "VortexSh":
                    self.dATK = dATK + 0.496 + (0.03+0.01*R)*5*2
                else:
                    self.dATK = dATK + 0.496 + (0.03+0.01*R)*5
        elif weapon == "Spine":
                self.baseATK = baseATK + 674
                self.CR = CR + (0.06+0.02*R)
        elif weapon == "Grasscutter":
                self.baseATK = baseATK + 608
                self.ER = ER + 0.551
                self.dATK =  dATK + (ER-1+0.25+0.05*R) * (0.21+0.07*R)/100
        elif weapon == "DM not Solo":
                self.baseATK = baseATK + 454
                self.CR  = CR + 0.368
                self.dATK = dATK + 0.12 + R * 0.04
        elif weapon == "DM solo":
                self.baseATK = baseATK + 454
                self.CR  = CR + 0.368
                self.dATK = dATK + 0.18 +0.06 *R
        elif weapon == "Blackcliff 0 Stack":
                self.baseATK = baseATK + 510
                self.dATK = dATK + (0.09 +0.03 *R) * 0
                self.CDMG = CDMG + 0.551
        elif weapon == "Blackcliff 1 Stack":
                self.baseATK = baseATK + 510
                self.dATK = dATK + (0.09 +0.03 *R) * 1
                self.CDMG = CDMG + 0.551
        elif weapon == "Blackcliff 2 Stack":
                self.baseATK = baseATK + 510
                self.dATK = dATK + (0.09 +0.03 *R) * 2
                self.CDMG = CDMG + 0.551            
        elif weapon == "Blackcliff 3 Stack":
                self.baseATK = baseATK + 510
                self.dATK = dATK + (0.09 +0.03 *R) * 3
                self.CDMG = CDMG + 0.551
        elif weapon == "CrescentPike":
                self.baseATK = baseATK + 565
        elif weapon == "Lithic 1 Liyue":
                self.baseATK = baseATK + 565
                self.dATK = dATK + 0.276 + (0.06 + R*0.01)
                self.CR = CR + (0.02 + 0.01 *R)        
        elif weapon == "Lithic 2 Liyue":
                self.baseATK = baseATK + 565
                self.dATK = dATK + 0.276 + (0.06 + R*0.01)*2
                self.CR = CR + (0.02 + 0.01 *R)*2
        elif weapon == "Lithic 3 Liyue":
                self.baseATK = baseATK + 565
                self.dATK = dATK + 0.276 + (0.06 + R*0.01)*3
                self.CR = CR + (0.02 + 0.01 *R)*3
        elif weapon == "Lithic 4 Liyue":
                self.baseATK = baseATK + 565
                self.dATK = dATK + 0.276 + (0.06 + R*0.01)*4
                self.CR = CR + (0.02 + 0.01 *R)*4
        elif weapon == "The Catch":
                self.baseATK = baseATK + 510
                self.ER = ER + 0.459
        elif weapon == "Starglitter":
                self.baseATK = baseATK + 510
                self.ER = ER + 0.459
        elif weapon == "Kitain Spear":
                self.baseATK = baseATK+ 565
        elif weapon == "Dragonspine Spear":
                self.baseATK = baseATK + 454
        elif weapon == "Royal Spear":
                self.baseATK = baseATK + 565
                self.dATK = dATK +0.276
                #I hate it here
        elif weapon == "Favonius Lance":
                self.baseATK = baseATK + 565
                self.ER = ER + 0.306
        elif weapon == "Dragonsbane Effect Off":
                self.baseATK = baseATK + 454
        elif weapon == "Dragonsbane Effect On":
                self.baseATK = baseATK + 454
                self.Edmg = Edmg + 0.16 + 0.04 * R
        elif weapon == "White Tassel":
                self.baseATK = baseATK + 401
                self.CR = CR + 0.234
        elif weapon == "Black Tassel":
                self.baseATK = baseATK + 354
        elif weapon == "Halberd":
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
        acount = [2, 2 , 2, 1, 1 ,1, 4]
        buff10 = [1, 1 , 1, 1, 0 ,0, 0]
        buff12 = [1, 1 , 1, 1, 0 ,0, 0]
        rotation1=0        
        if self.weapon == "PJWS":
                bonus = (1+self.Edmg+Bdmg+((self.R)*3+9)/100)
        else:
                bonus = (1+self.Edmg+Bdmg)
        for i  in range (0,7):

            rotation1 += acount[i]*hp*(bonus+as1[i])*(offmulti1+buff10[i]*ttds*0.48*self.baseATK+buff12[i]*1202*bennet)
        
        if self.weapon == "Kitain Spear":
            rotation1 += (e * 2 * (bonus-0.952+0.045+0.015*self.R))*offmulti1+(e * 2 * (bonus-0.952+0.045+0.015*self.R))*(offmulti1+ttds*0.48*self.baseATK+1202*bennet)
        else:
            rotation1 += (e * 2 * (bonus-0.952))*offmulti1+(e * 2 * (bonus-0.952))*(offmulti1+ttds*0.48*self.baseATK+1202*bennet)
        
        return  aux1 * rotation1 *CritMulti

   
a = Character(349,"PJWS",2,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
def bestbuild(a,submax,cratecap,bennet,ttds):
    aux = 0
    holder= []
    index = 0
    max = 0
    header = ['index','flatAtk','ATK%','CritRate%','CritDmg%','Damage']
    with open ('data.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        for i in range(4,36):
                for j in range (4,36):
                    for k in range (5,36):
                        for l in range (4,36):

                            if (i+j+k+l)==submax:
                                if not((i>36) or (j>36) or (k>36) or (l>36)):
                                    if (a.CR+k*3.9/100)<=1:
                                        y = deepcopy(a)
                                        y.substat(i,j,k,l)
                                        if y.CR <= cratecap:
                                            b1 = y.PerfectRotation(0.952,0.1,0,90,90,0,1,ttds,bennet)
                                            if b1 > max:
                                                max = b1
                                                maxi = index
                                                        
                                            b2 = [index, i, j, k, l]
                                            writer.writerow([index, i, j, k, l,b1])
                                            
                                            index += 1
                                            holder.append([b2,b1])                        
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
result = bestbuild(a,36,0.8,0,0)