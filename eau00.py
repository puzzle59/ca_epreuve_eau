#Fonctions
def asked_array():
    results=[]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i < j and j<k :
                    result=str(i)+str(j)+str(k)
                    results.append(result)
    return results
#Pas de Gestion d'erreur
#Pas de parsing

#Pas de résolution
#Affichage
for items in asked_array()[:-1]:
    #j'affiche tout les élèments du tableau sauf le dernier
    #pour ne pas qu'il y ait une virgule à la toute fin.
    print(items, end=",")
#j'affiche le dernier élément
print(asked_array()[-1])
