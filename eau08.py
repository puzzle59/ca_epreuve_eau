import sys
string=sys.argv[1]
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
print(is_only_numb(string))
