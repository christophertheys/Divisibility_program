# Integer divisibility program
user_input_for_integer = int(input("Enter an integer into the program"))
print("\n")

if user_input_for_integer % 2 == 0 and user_input_for_integer % 5 == 0:
    print("The number is divisible by 2 and 5", "\n")

elif user_input_for_integer % 2 == 0:
    print("The number is divisible by 2", "\n")

elif user_input_for_integer % 5 == 0:
    print("The number is divisible 5", "\n")

else:
    print("The number is not divisible by 2 or 5", "\n")

print("The number you have typed in is {}".format(user_input_for_integer))

# This is what I have just added!
