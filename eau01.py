#Fonctions
def asked_array_2():
    array=[0,1,2,3,4,5,6,7,8,9]
    for i in array:
        for j in array:
            for k in array:
                for l in array:
                    if (10*i+j)<(10*k+l):
                        #Trois test pour que l'affichage se fasse correctement
                        #D'abord pas d'espace au début mais virgule, puis espace et
                        #virgule, puis espace au début sans virgule pour le dernier
                        if i==0 and j ==0 and k== 0 and l==1:
                            print(str(i)+str(j)+" "+str(k)+str(l),end=',')
                        elif (str(i)+str(j))!="98":
                            print(" "+str(i)+str(j)+" "+str(k)+str(l),end=',')
                        else:
                            print(str(i)+str(j)+" "+str(k)+str(l))
#Affichage/résolution
asked_array_2()
