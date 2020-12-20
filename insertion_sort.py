
def insertion(array):
    length = len(array)
    for i in range(length-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
        
            if i!=0 and array[i-1] > array[i]:
                while array[i] < array[i-1] and i!=0:
                    array[i], array[i-1] = array[i-1], array[i]
                    i -=1
                 
    return array


print(insertion([5,7,7,5,5,5,1]))