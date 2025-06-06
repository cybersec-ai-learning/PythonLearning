print(2>3)
var_one = 1
var_two = 2
print(var_one < 1)
print(var_two >= var_one)

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message