import sys


def my_bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
#on prend un élément on le compare aux autres du tableau,
#s'il est plus grand on le déplace vers la droite
#et on fait ça avec tout les éléments
            if int(array[j]) > int(array[j+1]):
                c=array[j]
                array[j]=array[j+1]
                array[j+1]=c
    return array
if len(sys.argv[1:])> 0:
    array=sys.argv[1:]
    for item in array:
        try:
            int(item)
        except ValueError:
            sys.exit("que des nombres svp")
    print(my_bubble_sort(array))

else:
    sys.exit("fournissez un tableau")
