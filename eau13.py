import sys
#Tri sélection
def tri_selection(tab):
    n=len(tab)
    #on prend un élément qu'on considère min et on le compare aux autres
    #si on trouve plus petits on échange les valeurs
    for i in range(0,n-1):
        min=i
        for j in range(1+i,n):
            if int(tab[j]) <int(tab[min]):
                min=j
        if min!=i:
            c=tab[i]
            tab[i]=tab[min]
            tab[min]=c
        print(tab)
    return tab
#Parsing
if len(sys.argv[1:])> 0:
    array=sys.argv[1:]
    for item in array:
        try:
            int(item)
        except ValueError:
            sys.exit("que des nombres svp")
#Résolution
    resultat=tri_selection(array)
#affichage
    print(resultat)
