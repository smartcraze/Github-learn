# Initialize an empty tuple
my_tuple = ()

# Define the number of inputs you want
num_inputs = int(input("Enter the number of inputs: "))

# Loop to take multiple inputs and store them in the tuple
for i in range(num_inputs):
    value = int(input("Enter a value: "))
    # Convert the input to the appropriate data type if needed (e.g., int, float)
    # Add the input to the tuple using concatenation
    my_tuple += (value,)

# Print the resulting tuple
print("The tuple you created is:", my_tuple)
