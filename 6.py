# write a function to print those set of an array whose sum is equeal to 2\

def backtrack(arr,k):
    def solve(current, index, total):
        if index == len(arr):
            if total == k:
                print(current)
                return
            

                 # include element\\

        current.append(arr[index])
        solve(current,index + 1, total + arr[index])

           # exclude the element\
        current.pop()   


        solve(current,index + 1 , total)



    solve([],0,0)

backtrack([1,2,1],2)



