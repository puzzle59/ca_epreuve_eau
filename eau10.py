#rechercher le dernier argument dans un tableau constitué de tout les premiers
import sys
tableau=sys.argv[1:]
def index_last_one(un_tableau):
    item=un_tableau[-1]
    try :
        index=un_tableau[:-1].index(item)
    except ValueError:
        return -1
    else:
        return index
print(index_last_one(tableau))
