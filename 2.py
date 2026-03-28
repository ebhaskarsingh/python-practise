# write a function to print the digits in a number using recursion\\
def count_digit(num):
    if num == 0:
        return 0
    else:
        return (1+count_digit(num//10))
    

n = int(input("enter the number: "))
n = count_digit(n)
print(n)

# write a program to check whether the number is palindrome or not using recursion\\

def palindrome(num, rev=0):
    if num == 0:
        return rev
    return palindrome(num // 10, rev * 10 + num % 10)

n = int(input("enter: "))
reversed_num = palindrome(n)

if n == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")