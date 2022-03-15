import sys
def is_in(sone,stwo):
    if len(stwo)>= len(sone):
        return False
    else:
        for j in range(len(sone)-len(stwo)+1):
                if sone[j:j+len(stwo)] == stwo:
                    return True
        return False
if len(sys.argv[1:])== 2:
    try:
        sone=sys.argv[1]
        stwo=sys.argv[2]
    except ValueError:
        print("-1")
    else:
        print(is_in(sone,stwo))
else:
    print("-1")
