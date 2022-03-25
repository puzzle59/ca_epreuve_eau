import sys
string=sys.argv[1]
def is_char(char):
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

display(sys.argv[1])
