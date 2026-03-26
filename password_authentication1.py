# Slightly Stronger Password Authentication Program

# Create a password with minimum length check
saved_password = input("Create a password (min 6 characters): ")

if len(saved_password) < 6:
    print("Password too short. Please restart and try again.")
else:
    attempts = 3

    while attempts > 0:
        entered_password = input("Enter your password: ")

        if entered_password == saved_password:
            print("Login Successful")
            break
        else:
            attempts -= 1
            print("Incorrect password. Attempts left:", attempts)

    if attempts == 0:
        print("Access Denied. Too many failed attempts.")
