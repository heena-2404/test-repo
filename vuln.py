# Potential Bug (division by zero)
def calculate_average(numbers):
  if len(numbers) == 0:
    return 0  # Handle empty list better (avoid division by zero)
  else:
    return sum(numbers) / len(numbers)

# Potential Security Vulnerability (hardcoded password)
PASSWORD = "mysecretpassword"  # Store passwords securely (e.g., environment variables)

def authenticate(username, password):
  if username == "admin" and password == PASSWORD:
    return True
  else:
    return False

# Code Smell (duplicate code)
def print_message(message):
  print(message)

def log_message(message):  # Duplicate functionality with print_message
  print(message)

# Maintainability Issue (complex logic with nested ifs)
def process_order(order):
  if order.status == "pending":
    if order.payment_verified:
      ship_order(order)
    else:
      send_payment_reminder(order.customer)
  elif order.status == "shipped":
    # More complex logic here...
  else:
    raise ValueError("Invalid order status")

# Lack of Documentation (missing comments)
def mysterious_function(data):
  # No comments explaining what the function does or how the data is used
  # This makes it difficult to understand and maintain the code
  result = data * 2
  return result
