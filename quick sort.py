 
def partition(arr,left,right):
    pivot=arr[right]
    i=left
    j=right-1
    while i<j:
        while i<right and arr[i]<=pivot:
            i=i+1
        while j>left and arr[j]>=pivot:
            j=j-1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    print(arr)
    return i
arr=input("enter the list of numbers :").split() b 
arr=[int(x) for x in arr]
quicksort(arr,0,len(arr)-1)
print("sorted list:",end=" ")
print(arr)
    

