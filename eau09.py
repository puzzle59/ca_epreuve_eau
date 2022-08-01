#Entre min et max
import sys
#Fonction

def min_max(a,b):

    for item in range(a,b):
        print(item,end=" ")
##Parsing/gestion d'erreur
if len(sys.argv[1:]!=2:
    try:
        n1=int(sys.argv[1])
        n2=int(sys.argv[2])
    except ValueError:
        sys.exit("donner deux nombre")
else:
    sys.exit("deux nombre ni plus ni moins svp")
#Affichage
min_max(n1,n2)
# J'ignore pourquoi mais ça m'affiche None quand je print le tableau..
#car, je n'ai pas mis return dans la fonction
# autre idée; directement afficher via range
