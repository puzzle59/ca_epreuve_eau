import sys
if len(sys.argv[1:])== 1 :
    try:
        n=int(sys.argv[1])

    except ValueError:
        print("-1")
    else:
        def fibonnaci(n):
            if n<0:
                return -1
            elif n ==0:
                return 0
            elif n == 1 :
                return 1
            else :
                return fibonnaci(n-2)+fibonnaci(n-1)
        print(fibonnaci(n))
else:
    print("-1")
