import string

stringg = input("Enter a password: ")

if len(stringg) >= 12:
    has_alnum = any(char.isalnum() for char in stringg)
    has_special = any(char in string.punctuation for char in stringg)
    has_upper = any(char.isupper() for char in stringg)
    has_lower = any(char.islower() for char in stringg)

    if has_alnum and has_special and has_upper and has_lower:
        print("It's a strong password")
    else:
        print("It's not a strong password")
else:
    print("Password length should be at least 12 characters.")
