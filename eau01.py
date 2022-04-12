array=[0,1,2,3,4,5,6,7,8,9]
for i in array:
    for j in array:
        for k in array:
            for l in array:
                if (10*i+j)<(10*k+l):
                    if i==0 and j ==0 and k== 0 and l==1:
                        print(str(i)+str(j)+" "+str(k)+str(l),end=',')
                    elif (str(i)+str(j))!="98":
                        print(" "+str(i)+str(j)+" "+str(k)+str(l),end=',')
                    else:
                        print(str(i)+str(j)+" "+str(k)+str(l))
