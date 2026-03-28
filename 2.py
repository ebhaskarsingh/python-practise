# write a function to print the digits in a number using recursion\\
def count_digit(num):
    if num == 0:
        return 0
    else:
        return (1+count_digit(num//10))
    

n = int(input("enter the number: "))
n = count_digit(n)
print(n)