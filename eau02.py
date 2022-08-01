#Pour moi pas de problème d'argument possible argument
import sys
def arg_a_lenvers(args):
    liste_reverse=[]
    for i in range(1,len(args)):
        print(args[-i])
    print(args[0])

#Erreurs
if len(sys.argv[1:])==0:
    #Fonction pour quitter
    sys.exit("pas d'argument")
#Parsing
arguments=sys.argv[1:]
#Résolution / Affichage
arg_a_lenvers(arguments)
