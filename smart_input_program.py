# Smart Input Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Age categorization
if age < 18:
    category = "a minor"
elif age <= 60:
    category = "an adult"
else:
    category = "a senior citizen"

# Personalized message
print("\nHello", name + "!")
print("You are", category + ".")
print("It's great to know that you enjoy", hobby + ".")
