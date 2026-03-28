# write a funtion to print number from 1 to n using recursion\

def print_numbers(n):
    if n == 0:
        return 0
    print_numbers(n-1)
    print(n)


num = int(input("enter the number: "))
print_numbers(num)

# write a funtion to print numbers from n to 1 using recursion\\

def print_numbers(n):
    if n == 0:
        return 0
    print(n)
    print_numbers(n-1)

num = int(input("enter the numbers: "))
print_numbers(num)


# write a function to find the factorial of a number using recursion\\

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return  num*factorial(num-1)
    
n = int(input("enter the number: "))
n = factorial(n)
print(n)


# write a function to print the sum of nth natural number using recursion\\

def natural_number(num):
    if num == 0:
        return 
    if num == 1:
        return 1
    else:
        return num+natural_number(num-1)
    

n = int(input("enter the numbers: "))
n = natural_number(n)
print(n)



# write a function to print the sum of digits of a number using recursion\\

def sum_digits(num):
    num = str(num)
    total = 0

    for i in num :
        total+=int(i)

    return total

n = int(input("enter the number: "))
n = sum_digits(n)
print(n)


# write a function to print the nth fabonacci number\\\

def fabonacci(num):
    first = 0
    second = 1
    sum  = 0

    for i in range(1,num):
        
        sum = first+second
        first = second
        second = sum

    return second

n = int(input("enter the number: "))
n = fabonacci(n)
print(n)