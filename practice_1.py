def switch(i, j, arr):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]


def partition(elements, start, end):
    pivot_idx = start
    pivot = elements[start]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start +=1
        
        while elements[end] > pivot:
            end -=1
        if start < end:
            switch(start, end, elements)

    switch(pivot_idx, end, elements)

    return end

def qs(elements, start, end):
    if start < end:
        part = partition(elements, start,end)
        qs(elements, start, part -1)
        qs(elements, part+1, end)


def binarySearch(arr, target):
    size = len(arr)
    if size == 1:
        if target == arr[0]:
            return 0
        else:
            return -1
        
    left = 0
    right = size -1
    
    while left <=right:
        mid = left +(right-left/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
            
        else:
            left = mid +1
    return -1

    

if __name__ == "__main__":
    elements = [6, 5, 4, 11, 2, 3, 44]
    qs(elements, 0, len(elements)-1 )
    print(elements)
    print(binarySearch(elements,5))

