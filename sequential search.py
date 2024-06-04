def ss(a,n,t):
    for i in range (0, n-1):
        if a[i]==t:
            return i
    return -1
a=[1,3 ,22, 4,5]

t=3

print("index:",ss(a,len(a),t))