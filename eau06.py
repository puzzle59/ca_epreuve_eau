import sys
#Fonctions
def is_char(char):

    #est-ce que le caractère est une lettre? avec table ascii
    if (ord(char)>=65 and ord(char)>= 90) or (ord(char)>=97 and ord(char)<=122):
        return True
    else:
        return False
def display(string):
    a= 1
    for item in string:
        if ord(item)==32:
            print(item,end='')
        if is_char(item):
            if a==1:
                print(item.upper(),end='')
                a= -1
            else:
                print(item.lower(),end='')
                a=1
#Gestion d'Erreur
        else:
            sys.exit("lettres uniquement")
#parsing
array=sys.argv[1:]
full_string=""
for string in array:
    full_string+=' '+string
#Affichage
display(full_string)
