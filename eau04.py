#premier nombre premier superieur au nbre passe en param
import sys
#Fonctions
def is_prime(m):
    if m== 0 or m ==1 or m == 2:
        return False
    for i in range(2,m-1):
        if m%i == 0:
            return False
    return True
def upper_prime(k):
    if is_prime(k):
        k+=1
    while is_prime(k)!=True:
        k+=1
    return k
#Gestion d'erreur/parsing

try :
    n=int(sys.argv[1])
except ValueError:
    sys.exit("-1")
#affichage
else:
    if n <0:
        sys.exit("-1")
print(upper_prime(n))
