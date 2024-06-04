def bs(a,n,t):
    l=0
    h=n-1
    
    while l<=h:
        m=(l+h)//2
        if a[m]==t:
            return m
        elif a[m]<t:
            l=m+1
        else:
            h=m-1
    return -1

arr = [1, 3, 4, 7, 9]
n = len(arr)
target = 4
print("index :",bs(arr,n,target))