import sys
#Fonction
def fibonnaci(n):
    if n<0:
        return -1
    elif n ==0:
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonnaci(n-2)+fibonnaci(n-1)
if len(sys.argv[1:])== 1 :
#Parsing/gestion d'erreur
    try:
        n=int(sys.argv[1])

    except ValueError:
        sys.exit("-1")
#Affichage
else:
    sys.exit("-1")

print(fibonnaci(n))
