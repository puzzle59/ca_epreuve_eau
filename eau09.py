#Entre min et max
import sys
n1=int(sys.argv[1])
n2=int(sys.argv[2])
def min_max(a,b):
    tableau=[]
    for i in range(a,b):
        tableau.append(i)
    for item in tableau:
        print(item,end=" ")
min_max(n1,n2)
# J'ignore pourquoi mais ça m'affiche None quand je print le tableau..
#car, je n'ai pas mis return dans la fonction
# autre idée; directement afficher via range
