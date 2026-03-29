# write a code to find the subsets of an array using backtracking\\

def subset(arr):
    def solve(index,current):
        if index == len(arr):
            print(current)
            return
        

        # include the item\\
        current.append(arr[index])
        solve(index+1,current)


        current.pop()


        # skip the item\\

        solve(index+1,current)

    solve(0,[])


subset([1,2,3])