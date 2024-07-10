def calculate_rectangle(width, height):
  """Calculates the area and perimeter of a rectangle."""

  # Check for non-positive values
  if width <= 0 or height <= 0:
    print("Error: Width and height must be positive values.")
    return

  area = width * height
  perimeter = 2 * (width + height)

  print("Area of the rectangle:", area)
  print("Perimeter of the rectangle:", perimeter)

# Get user input for width and height
try:
  width = float(input("Enter the width of the rectangle: "))
  height = float(input("Enter the height of the rectangle: "))
except ValueError:
  print("Error: Invalid input. Please enter numbers.")
  exit()

# Call the function to calculate
calculate_rectangle(width, height)
