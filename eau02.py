#à faire : quitter le programme is pb argument
import sys
def arg_a_lenvers(args):
    liste_reverse=[]
    for i in range(1,len(args)):
        print(args[-i])
    print(args[0])
arg_a_lenvers(sys.argv[1:])
