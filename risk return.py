IA = 100000 #Investment amount
pA = 0.05 #Probability return is +50%
pB = 0.25 #Probability return is +30%
prA = 0.5 #Probable return for pA
prB = 0.3 #Probable return for pB

ER = pA * prA * pB * prB + 0.4 * (pA+pA) + pB * (-pA-pA) + pA * (-prA)   #Expected return calculation

