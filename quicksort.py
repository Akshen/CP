def swap(a, b, arr):
    if a!=b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot_idx = start
    pivot = elements[pivot_idx]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start +=1

        while elements[end] > pivot:
            end -=1

        if start < end:
            swap(start, end, elements)
    
    swap(pivot_idx, end, elements)
    
    return end

def quicksort(elements, start, end):
    if start < end:
        parted = partition(elements, start, end)
        quicksort(elements, start, parted -1)
        quicksort(elements, parted + 1, end)



if __name__ == "__main__":
    elements = [3,4,2,8,1,10,11,5,41,12]
    quicksort(elements, 0, len(elements)-1)
    print(elements)
