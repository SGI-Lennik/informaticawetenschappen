# functie bereken_term_meetkundige_rij(n, u1, q):
#     u_n = u1
#     ALS n == 1 DAN
#         return u_n
#     ANDERS
#         HERHAAL n-1 keer
#           u_n = u_n * q        
#         STOP
#         return u_n

def bereken_term_meetkundige_rij(n, u1, q):
    un = u1
    if n == 1:
        return un
    else:
        for n in range(2,n+1):
            un = un * q

        return un

print(bereken_term_meetkundige_rij(5, 3, 2))
print(3*pow(2, 4))