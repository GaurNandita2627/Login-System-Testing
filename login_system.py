import json
import os

FILE_NAME = "users.json"

# ---------------- LOAD USERS ----------------
def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    else:
        return {
            "admin": {"password": "1234", "email": "admin@gmail.com"}
        }

# ---------------- SAVE USERS ----------------
def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file)

users = load_users()

attempts_limit = 3

print("\n==============================")
print("   PRO LOGIN SYSTEM v2.0     ")
print("==============================\n")

print("1. Login")
print("2. Register")
print("3. Exit")

choice = input("\nEnter choice: ")

# ---------------- REGISTER ----------------
if choice == "2":
    username = input("Create username: ")

    if username in users:
        print("User already exists ❌")
    else:
        password = input("Create password: ")
        email = input("Enter email: ")

        users[username] = {
            "password": password,
            "email": email
        }

        save_users(users)

        print("\nAccount created successfully ✅")

# ---------------- LOGIN ----------------
elif choice == "1":

    username = input("\nEnter username: ")

    if username in users:

        attempts = attempts_limit

        while attempts > 0:

            password = input("Enter password: ")

            if password == users[username]["password"]:
                print("\nLogin Successful ✅")
                print("Welcome", username)

                # MENU
                while True:
                    print("\n===== MENU =====")
                    print("1. View Profile")
                    print("2. Logout")

                    option = input("Choose option: ")

                    if option == "1":
                        print("\n--- PROFILE ---")
                        print("Username:", username)
                        print("Email:", users[username]["email"])

                    elif option == "2":
                        print("\nLogged out 👋")
                        break

                    else:
                        print("Invalid option ❌")

                break

            else:
                attempts -= 1
                print("Wrong password ❌ Attempts left:", attempts)

        if attempts == 0:
            print("\nAccount Locked 🔒")

    else:
        print("User not found ❌")

# ---------------- EXIT ----------------
elif choice == "3":
    print("Exited system 👋")

else:
    print("Invalid choice ❌")
    