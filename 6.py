def backtrack(arr,k):
    def solve(current, index, total):
        if index == len(arr):
            if total == k:
                print(current)
            return
            

        # include element
        current.append(arr[index])
        solve(current,index + 1, total + arr[index])

        # backtrack
        current.pop()   

        # exclude element
        solve(current,index + 1 , total)

    solve([],0,0)

backtrack([1,2,1],3)


# write a function to print the subsequence of an array whose target is k and elements can be reused\\

def backtrack(arr,target):
    def solve(current, index, total):
        if total == target:
            print(current)
            return
        if index == len(arr) or total>target:
            return
        


        # include element\\\
        current.append(arr[index])
        solve(current, index,total+arr[index])


        # backtrack\\

        current.pop()


        # exclude element \\

        solve(current, index+1, total)


    solve([],0,0)

backtrack([2,3,6,7],7)


# combination sum , where element can not be reused and handles the duplicate\\

def backtrack(arr , target):
    arr.sort()
    def solve(current, index, total):
        if total == target:
            print(current)
            return
        if total >target:
            return
        
        for i in range(index, len(arr)):
              if i > index and arr[i] ==arr[i-1]:
                  continue
              
              current.append(arr[i])



              solve(current, index+1 , total+arr[i])


              current.pop()


    solve([],0,0)

backtrack([10,1,2,7,6,1,5],8)
            

        
