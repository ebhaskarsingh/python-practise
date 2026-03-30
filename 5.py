# writa function to print all the permutation of an array using backtracking\\

def permutation(arr):
    def solve(current):
        if len(current) == len(arr): # it is base case , when all the item add to current then we will print the current and return

            print(current)
            return
        
        for i in arr:
            if i not in current:
                current.append(i) # to add the item in current
                solve(current) # backtracking

                current.pop() # to remove the last item from current and try the next item in arr
                
    solve([]) # it will tell the solve function to start with index 0 and empty current list


permutation([1,2,3])