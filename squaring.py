# Take input from the user to create a list of numbers
num_list = []
num_of_elements = int(input("Enter the number of elements in the list: "))

for i in range(num_of_elements):
    num = float(input(f"Enter element {i + 1}: "))  # Convert input to float for decimal values
    num_list.append(num)

# Create a list of squares
squared_list = [num ** 2 for num in num_list]

# Combine the original numbers and their squares in a new list
combined_list = list(zip(num_list, squared_list))

# Print the combined list
print("Original Numbers and Their Squares:")
for pair in combined_list:
    print(f"Number: {pair[0]}, Square: {pair[1]}")
