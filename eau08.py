import sys

def is_numb(char):
    try:
        chiffre=int(char)
    except ValueError:
        return False
    else:
            return True
def is_only_numb(string):
    boule=True
    for item in string:
        if not is_numb(item):
            boule=False
    if boule:
        return "c'est ok , que des chiffres dans cette string"
    else:
        return "Nicht gut nicht gut"
if len(sys.argv[1:])!=1:
    sys.exit("Un seul argument et string")
#Parsing
string=sys.argv[1]
#Affichage
print(is_only_numb (string))
