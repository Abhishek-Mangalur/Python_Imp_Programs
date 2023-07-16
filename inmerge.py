def insertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key
        
def mergeSort(arr):
    L = []
    R = []
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        
    i = j = k = 0
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
            
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()
    
while(True):
    print("1. Insertion Sort")
    print("2. Merge Sort")
    ch = input("\nEnter the choice: ")
    
    if ch == "1":
        arr = list(map(int, input("Enter the elements of list: ").strip().split()))
        print(arr)
        insertionSort(arr)
        printList(arr)
    elif ch == "2":
        arr = list(map(int, input("Enter the elments of list: ").strip().split()))
        mergeSort(arr)
        printList(arr)
    else:
        exit(0)