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