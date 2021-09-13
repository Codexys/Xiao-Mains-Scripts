# Xiao-Mains-Scripts

"The script ain't the prettiest, it consists of three simple parts:
The class definition of a Character object that will be assigned with multiple stats relevant to the calculations as well as a sort of switch case structure to modify the stats based on weapon and weapon refinement.

Two methods to this class, one that modifies the values of certain stats parameters based on four input arguments. The stats to be increased by this are flat ATK, ATK%, C.RATE% and C.DMG%, since they are the offensive stats that yield the highest dps increase. (A high HP% roll gives less than a high flat atk roll even at R5 Homa under 50%)

The other one calculates the damage done when Xiao has lvl 10 AA, Q and E, on a rotation using perfect frame plunge at 75 frames and considering there's a hitlag window to perform 14 High plunges, as well as 4 Es from start and end, the method dynamically accounts for TTDS buff, Bennet buff and can be easily modified to account for buffs of shorter or longer duration with some more work.
The last and ugliest part of the process is the brute force sorting method. It consists of building an instance character and assigning him the base values, then we start iterating every possible combination of substats while using the substat method and calculate damage per rotation using the other method. Finally we sort using one of the most basic sorting algorithms to exist, and conditionally skipping every substat iteration that doesn't follow a guideline of rules that are as follows:
-The max sub count can't surpass a Cap given as an argument to the function call of the script. (This allows us to cap the sub count for multiple Tables)
-Each sub has a floor of 4 rolls with one crit sub having 5 (They all need to be max roll on each artifact except for the ones coinciding to their main stat)
-Each sub can only roll a max of 24 times (this comes from each arti having a single roll  already and being able to roll 5 times which makes up to 6 x 4 since all subs have a mainstat related to each other except for the non mainstat crit sub, which will be able to roll up to 30 times)

For this reason we iterate 30 times for each sub, discarding the iterations that don't follow this rules and finally getting the max possible distribution of stats that yield the maximum possible damage for each weapon.
Rinse and repeat for each spear at multiple subcounts, with different buffs. And you got yourself a nifty table to show everyone how White tassel has a build that beats Engulfing spear on Xiao, so please stop asking me if it's good on him"		
