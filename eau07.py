import sys
string=sys.argv[1]
#gérer les types d'arguments
def is_char(char):
    if (ord(char)>=65 and ord(char)>= 90) or (ord(char)>=97 and ord(char)<=122):
        return True
    else:
        return False

def is_string(string):
    return True


#faire le tri dans le nom des variables
def display(string):
    if is_string(string):
        string=string[0].upper()+ string[1:]
        print(string)
display(string)
