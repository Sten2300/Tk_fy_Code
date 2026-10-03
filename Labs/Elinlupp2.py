# efter https://electronics.stackexchange.com/questions/601136/ltspice-modeling-an-led
from sympy import symbols, ln, exp, solve, Eq
vd, id, N, ISAT, RS = symbols( "vd id N ISAT RS" )
# diodens temperatur i °C
TA = 25 

# ta tre mätpunkter från diodens karakteristiska I(V)-kurva, 
# ange spänningen i volt och strömmen i ampere
POINTS = [
    {vd:2.45, id:1e-5},
    {vd:2.88,  id:1e-3},
    {vd:3.5, id:0.017}
]

#==============================================================================================
# låt python räkna...
VT = 8.61733034e-5 * ( 273.15 + TA )

EQS = []
for i in range(3):
    EQS.append( Eq( POINTS[i][vd], RS*POINTS[i][id] + N*VT*ln(POINTS[i][id]) - N*VT*ISAT ) )
ANS = solve( EQS, [ RS, N, ISAT ] )[0]

print(f"""
.model MYDIODE D(
+ IS={exp(ANS[2]):.3e}
+ RS={ANS[0]:.3e}
+ N={ANS[1]:.3e})
""")