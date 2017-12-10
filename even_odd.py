def even_odd(num):
    a = num % 2
    if a == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


user_input = int(input("Enter a number: "))
even_odd(user_input)
