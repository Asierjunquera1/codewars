def cube(n):
    a=['']*n*2
    for i in range(0,n):
        a[i]=a[i]+(' '*(n-i-1))+'/\\'*abs(i+1)+ '_\\'*n
    for i in range(n,2*n):
        a[i]=a[i]+(' '*abs(n-i))+'\\/'*abs(2*n-i)+ '_/'*n
    a='\n'.join(a)
    return a
