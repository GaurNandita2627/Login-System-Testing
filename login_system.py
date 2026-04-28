import json
import os
import hashlib
from datetime import datetime

FILE = "users.json"
LOG_FILE = "login_history.txt"

# ---------- PASSWORD HASH ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- LOAD USERS ----------
def load_users():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# ---------- SAVE USERS ----------
def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f)

# ---------- LOG LOGIN ----------
def log_login(username):
    with open(LOG_FILE, "a") as f:
        f.write(f"{username} logged in at {datetime.now()}\n")

# ---------- REGISTER ----------
def register(users):
    print("\n--- REGISTER ---")
    username = input("Enter username: ")

    if username in users:
        print("User already exists ❌")
        return

    password = input("Enter password: ")
    email = input("Enter email: ")

    users[username] = {
        "password": hash_password(password),
        "email": email
    }

    save_users(users)
    print("Account created successfully ✅")

# ---------- LOGIN ----------
def login(users):
    print("\n--- LOGIN ---")
    username = input("Enter username: ")

    if username not in users:
        print("User not found ❌")
        return

    attempts = 3

    while attempts > 0:
        password = input("Enter password: ")

        if hash_password(password) == users[username]["password"]:
            print("\nLogin Successful ✅")
            print("Welcome", username)

            log_login(username)
            dashboard(username, users)
            return

        else:
            attempts -= 1
            print("Wrong password ❌ Attempts left:", attempts)

    print("Account Locked 🔒")

# ---------- DASHBOARD ----------
def dashboard(username, users):
    while True:
        print("\n===== DASHBOARD =====")
        print("1. View Profile")
        print("2. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            print("\n--- PROFILE ---")
            print("Username:", username)
            print("Email:", users[username]["email"])

        elif choice == "2":
            print("Logged out 👋")
            break

        else:
            print("Invalid option ❌")

# ---------- MAIN ----------
def main():
    users = load_users()

    while True:
        print("\n===== PRO LOGIN SYSTEM =====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            login(users)

        elif choice == "2":
            register(users)

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice ❌")

main()
