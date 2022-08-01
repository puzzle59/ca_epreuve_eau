import sys
#Fonctions
def is_in(sone,stwo):
    if len(stwo)>= len(sone):
        return False
    else:
#je me balade dans le premier mot , en séquencant avec les motifs
#de la taille du second mot

        for j in range(len(sone)-len(stwo)+1):
    #plus un car range exclus le dernier
            if sone[j:j+len(stwo)] == stwo:
                return True
        return False
#Parsing /gestion d'erreur
if len(sys.argv[1:]) == 2:
    try:
        sone=sys.argv[1]
        stwo=sys.argv[2]
    except ValueError:
        sys.exit("-1")

else:
    print("-1")
#Affichage
print(is_in(sone,stwo))
