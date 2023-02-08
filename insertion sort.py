def insertionsort(a):
    for i in range(1,len(a)):
        j=i
        while (a[j-1]>a[j] and j>0):
            t=a[j-1]
            a[j-1]=a[j]
            a[j]=t
            j=j-1
    print(a)
a=[2,56,78,45,98,76,21,20]
insertionsort(a)
