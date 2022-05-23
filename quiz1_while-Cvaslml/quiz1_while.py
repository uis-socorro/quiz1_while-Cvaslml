"""Quiz - while, capitales"""

print("--------------------------------------")
print("----------Inversion Capital-----------")
print("--------------------------------------")

#Processing
c1 = 0.03 
c2 = 0.04
c3 = c1 + c2
m = 0
while ( c1 + c2 < c3):
    c1 = 0.03 * m
    c2 = 0.04 * m
    c3 = c1 + c2
    m = m + 1 

#Output
print("Pueden realizar el negocio que desean en el mes: " + str(m))