def fun1(n,num):
    res=n
    tmp=n
    for i in range(1,num):
        tmp=tmp*10+n
        res+=tmp
    print(res)
fun1(2,3)