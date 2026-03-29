# write a recursive function to place the 3 numbers in all possible way using backtracking\\

def placing_numbers(l,index= 0,current = []):
    if index == len(l):
        print(current)
        return
    
    for num in l:
        if num not in current:
            current.append(num)
            placing_numbers(l,index, current)
            current.pop()


list = [1,2,3]
placing_numbers(list)