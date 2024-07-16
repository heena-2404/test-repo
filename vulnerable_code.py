# Potential SQL Injection Vulnerability
user_input = input("Enter your username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "'"
cursor.execute(query)

# Potential OS Command Injection Vulnerability (avoid using os.system)
user_command = input("Enter a command to execute: ")
os.system(user_command)

# Hardcoded password (store passwords securely)
PASSWORD = "mysecretpassword"

# Unvalidated user input (can lead to XSS attacks)
user_message = input("Leave a message for others: ")
print(user_message)
