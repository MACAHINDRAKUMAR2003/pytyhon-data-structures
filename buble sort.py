def bubblesort(a):
    n=len(a)
    swap=False
    for i in range(n-1):
        for j in range(1,n-i-1):
            if (a[j]>a[j+1]):
                swap=True
                a[j],a[j]=a[j+1],a[j]
            if not swap:
                return
a=[44,67,5,45,33,55,45,5456,45]
bubblesort(a)
print(a)
print("sorted array")
