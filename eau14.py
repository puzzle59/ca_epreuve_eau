import sys

#Fonctions
def invert_two_words(tab_2_element):
    #permet d'inverser deux mots dans un tableau , selon ordre ascii
    i=0
    while ord(tab_2_element[0][i])==ord(tab_2_element[1][i]):
        i+=1
    if ord(tab_2_element[0][i])>ord(tab_2_element[1][i]):
        #si ordre ascii pas croissant on échange
        #on va comparer aussi loin que nécessaire si égalité au début
        c=tab_2_element[0]
        tab_2_element[0]=tab_2_element[1]
        tab_2_element[1]=c
    return tab_2_element


def ascii_sort(array):
    #inspiré du tri à bulle
    #on parcourt le tableau et à chaque fois qu'on trouve plus grand
    #la fonction inverse les deux élements
    for i in range(len(array)):
        for j in range(len(array)-1-i):
                array[j:j+2]=invert_two_words(array[j:j+2])

                # j+2 car membre de droite exclus ? Oui
    return array
#parsing
array=sys.argv[1:]
print(ascii_sort(array))
