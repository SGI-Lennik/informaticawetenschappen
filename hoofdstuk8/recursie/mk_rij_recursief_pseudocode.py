# functie bereken_term_meetkundige_rij(n, u1, q):
#     ALS n == 1 DAN
#         return u1
#     ANDERS
#         return q * bereken_term_meetkundige_rij(n - 1, u1, q)

def bereken_term_meetkundige_rij(n, u1, q):
    if n == 1:
        return u1
    else:
        return q * bereken_term_meetkundige_rij(n-1, u1, q)

print(bereken_term_meetkundige_rij(5, 3, 2))
print(3*pow(2, 4))