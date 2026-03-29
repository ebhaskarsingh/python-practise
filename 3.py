# write a recursive function to print all the subset of an array using backtracking\\

def subsets(arr, index=0, current=[]):
    # base case
    if index == len(arr):
        print(current)
        return
    
    # include element
    subsets(arr, index + 1, current + [arr[index]])
    
    # exclude element
    subsets(arr, index + 1, current)


arr = [1, 2, 3]
subsets(arr)


# another way to do it\\

def subset(arr,index = 0,current = []):
    if index == len(arr):
        print(current)
        return
    # this will include the number\

    subset(arr,index+1,current+ [arr[index]])

    # this will exclude the number\\

    subset(arr,index+1,current)

array = [1,2,3]
subset(array)
