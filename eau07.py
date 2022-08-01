import sys

#gérer les types d'arguments
def is_char(char):
    if (ord(char)>=65 and ord(char)>= 90) or (ord(char)>=97 and ord(char)<=122):
        return True
    else:
        return False

def is_string(string):
    for char in string:
        if not is_char(char):
            return False
    return True

#gestion d'Erreur
#Problème gestion d'argument: guillemets ou pas , python donne un caractère
#string au arguments qu'il reçoit
if len(sys.argv[1:])!=1:
    sys.exit("Un seul argument et string")
def display(string):
    a= 1
    for item in string:
        if ord(item)==32 or ord(item)==44 or ord(item)==9:
            print(item,end='')
            a=1

        if is_char(item):
            if a==1:
                print(item.upper(),end='')
                a=-1
            elif a==-1:
                print(item.lower(),end='')
        else:
            print(item,end='')
#parsing
string=sys.argv[1]
#Affichage
display(string)
#J'ai remarqué un truc bizarre dans la ligne de commande,
#quand on met double "!" , cela répète l'argument en quelque sorte et cela ne fonctionne plus
