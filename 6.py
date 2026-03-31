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