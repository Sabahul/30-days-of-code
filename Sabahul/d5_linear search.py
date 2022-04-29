def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1
array = [29, 43, 23, 54, 19]
x = 54
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
    
    
   ### Output.. 
    ## Element found at index:  3
