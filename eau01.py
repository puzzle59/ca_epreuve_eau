"""Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


Exemples d’utilisation :
$> python exo.py
00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
$>
"""
array=[0,1,2,3,4,5,6,7,8,9]
for i in array:
    for j in array:
        for k in array:
            for l in array:
                if (10*i+j)<(10*k+l):
                    if (str(i)+str(j))!="98":
                        print(" "+str(i)+str(j)+" "+str(k)+str(l),end=',')
                    else:
                        print(str(i)+str(j)+" "+str(k)+str(l))
