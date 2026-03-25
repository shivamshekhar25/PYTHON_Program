def check_even(num):   # parameterised function
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if check_even(n):
    print("Number is Even")
else:
    print("Number is Odd")