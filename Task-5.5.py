import random
s=random.randint(1,100)
print(s)
print("You have 10 attempts to guess it")
i=0
for i in range(11):
    value=int(input("Enter a number: "))
    if value>s:
        print(f" Too high! Attempts left:{10-i} ")
    elif value<s:
        print(f"Too low! Attempts left:{10-i} ")
    elif value==s:
        print(f"Congratulations! You guessed the number in {i} attempts.")
        break
else:
    print("Value entered is invalid")




