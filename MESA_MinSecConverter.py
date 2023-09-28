# Prompt the user to enter an integer in seconds
seconds = eval(input("Enter an integer in seconds: "))

# Get the minutes and seconds of the integer
minutes = seconds // 60

# Get the minutes in seconds
remaining_Seconds = seconds % 60

# Display the minutes and seconds
print(f"{seconds} seconds is {minutes} minutes and {remaining_Seconds} seconds")


