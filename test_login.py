# ==============================
# LOGIN SYSTEM + TESTING PROJECT
# ==============================

# -------- USERS DATABASE --------
users = {
    "admin": "1234",
    "veronica": "pass123",
    "student": "bca2026"
}

# -------- LOGIN FUNCTION --------
def login(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False


# -------- TEST CASES --------
def run_tests():
    print("\n===== RUNNING TEST CASES =====\n")

    test_cases = [
        ("admin", "1234", True),
        ("admin", "wrong", False),
        ("wronguser", "1234", False),
        ("veronica", "pass123", True),
        ("student", "wrongpass", False),
    ]

    test_number = 1

    for username, password, expected in test_cases:
        result = login(username, password)

        if result == expected:
            print(f"Test {test_number}: PASS ✅")
        else:
            print(f"Test {test_number}: FAIL ❌")

        test_number += 1


# -------- MAIN PROGRAM --------
print("1. Login")
print("2. Run Tests")
print("3. Exit")

choice = input("\nEnter choice: ")

if choice == "1":
    username = input("Enter username: ")
    password = input("Enter password: ")

    if login(username, password):
        print("Login Successful ✅")
    else:
        print("Login Failed ❌")

elif choice == "2":
    run_tests()

elif choice == "3":
    print("Exited 👋")

else:
    print("Invalid choice ❌")