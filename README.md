# searching-in-python

In this we are looking at sequential search and binary search.
Pesudocode:

a. Sequential Search-

    function sequentialSearch(arr, n, target)
   
                          for i = 0 to n-1
                          
                                if arr[i] == target
                                
                                      return i
                          return -1

b. Binary Search-

           function binarySearch(arr, n, target)
           
                 low = 0
                 
                 high = n - 1
                 
                 while low <= high
                 
                       mid = (low + high) // 2
                       
                       if arr[mid] == target
                       
                              return mid
                              
                       elif arr[mid] < target
                       
                              low = mid + 1
                              
                       else
                              high = mid - 1
                              
                 return -1


    
