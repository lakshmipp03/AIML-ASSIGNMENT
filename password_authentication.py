# Simple Password Authentication Program

# Set the password
saved_password = input("Create a password: ")

# Ask user to enter password again
entered_password = input("Enter your password: ")

# Check if password matches
if entered_password == saved_password:
    print("Login Successful")
else:
    print("Incorrect Password. Access Denied")
