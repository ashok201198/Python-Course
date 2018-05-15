
def factorize(number):
    li=[]
    if number<=0:
        raise ValueError
    if type(number).__name__!="int":
        raise TypeError
    if number<=1:
        return []
    c=0
    i=2
    while number!=1:
        if number%i==0:
            c+=1
            number=number//i
            if number==1:
                li.append((i,c))
                break
        else :
            if c!=0:
                li.append((i,c))
            c=0
            i+=1
    return li

def get_hcf(list1,list2):
    if list1==[] or list2==[]:
        return []
    res=[]
    for (i,j) in list1:
        for(k,l) in list2:
            if i==k:
                res.append((i,min(j,l)))
    return res
def get_lcm(list1,list2):
    if list1==[] :
        return list2
    elif list2==[]:
        return list1
    res=[]
    for (i,j) in list1:
        for(k,l) in list2:
            if i==k:
                res.append((i,max(j,l)))
    for (i,j) in list1:
        if [(k,l) for (k,l) in res if k==i]==[]:
            res.append((i,j))
    for (i,j) in list2:
        if [(k,l) for (k,l) in res if k==i]==[]:
            res.append((i,j))
    res.sort(key=lambda x:x[0])
    return res

def multiply(list1,list2):
    if list1==[] :
        return list2
    elif list2==[]:
        return list1
    res=[]
    for (i,j) in list1:
        for(k,l) in list2:
            if i==k:
                res.append((i,j+l))
    for (i,j) in list1:
        if [(k,l) for (k,l) in res if k==i]==[]:
            res.append((i,j))
    for (i,j) in list2:
        if [(k,l) for (k,l) in res if k==i]==[]:
            res.append((i,j))
    res.sort(key=lambda x:x[0])
    return res