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
                self.dATK =  dATK + (ER-1+0.25+0.05*R) * (0.21+0.07*R)/100
        
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

    def PerfectRotation(self,Bdmg,res,resShred,charlvl,enemylvl,defShred,Average):
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
        offmulti1 =(self.baseATK * (1 + self.dATK)+ self.flatATK)*CritMulti
        hp = 4.0402
        e = 4.5504
        as1 = [0.05, 0.1, 0.15, 0.2,0.25]
        acount = [2, 2 , 3, 2, 4]

        rotation1=0        
        if self.weapon == "PJWS":
                bonus = (1+self.Edmg+Bdmg+((self.R)*3+9)/100)
                for i  in range (0,5):
                    rotation1 += acount[i]*hp*(bonus+as1[i])
                rotation1 += e * 4 * (bonus-0.952)
        else:
                bonus = (1+self.Edmg+Bdmg)
                for i  in range (0,5):
                    rotation1+= acount[i]*hp*(bonus+as1[i])
                rotation1 += e * 4 * (bonus-0.952)
        return  aux1 * rotation1 *offmulti1

   
a = Character(349,"PJWS",2,311,0.466+0.18, 0.242 , 0.5+0.622 , 0.616 , 1+6.48/100*3 )
def bestbuild(a,submax):
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
                                        b1 = y.PerfectRotation(0.952,0.1,0,90,90,0,1)
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
    var = [a.weapon+" R"+str(a.R) , e[0][1],e[0][2],e[0][3],e[0][4],(a.baseATK*(a.dATK+1))+a.flatATK,a.CR,a.CDMG,max]
    return var
result = bestbuild(a,36)