results=[]
for i in range(10):
    for j in range(10):
        for k in range(10):
            if i < j and j<k :
                result=str(i)+str(j)+str(k)
                results.append(result)
for items in results[:-1]:
    print(items, end=",")
print(results[-1])
