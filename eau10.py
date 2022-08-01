#rechercher le dernier argument dans un tableau constitué de tout les premiers
import sys
#Fonctions
def index_last_one(un_tableau):
    item=un_tableau[-1]
    try :
        index=un_tableau[:-1].index(item)
    except ValueError:
        sys.exit("-1")
    else:
        return index
if len(sys.argv[1:])<2:
    sys.exit("au moins deux mots")
#parsing
tableau=sys.argv[1:]
#Affichage
print(index_last_one(tableau))
