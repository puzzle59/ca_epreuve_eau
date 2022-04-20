#diff minimum
import sys
script_arg=sys.argv[1:]

def diff_min(tableau):
    tab_diff=[]
    for digit in tableau:
        index=tableau.index(digit)
#Je prends un nombre du tableau et je le compare à tous le suivants.
#Donc le tableau commence à index +1
        for other_digit in tableau[index+1:]:
            diff= abs(int(digit) - int(other_digit))
            tab_diff.append(diff)
    return min(tab_diff)

print(diff_min(script_arg))
