#premier nombre premier superieur au nbre passe en param
import sys
def is_prime(m):
    if m== 0 or m ==1 or m == 2:
        return False
    for i in range(2,m-1):
        if m%i == 0:
            return False
    return True
def upper_prime(k):
    if k<0:
        return -1
    while is_prime(k)!=True:
        k+=1
    return k
try :
    n=int(sys.argv[1])
except ValueError:
    print("-1")
else:
    print(upper_prime(n))
# 
# for i in range(25):
#     print(f"{i}:{is_prime(i)}",end='//')
