print(2>3)
var_one = 1
var_two = 2
print(var_one < 1)
print(var_two >= var_one)

#if condition
def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message
print(evaluate_temp(39))

#if-else conditions
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message
print(evaluate_temp_with_else(30))

#if-elif-else conditions
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message
print(evaluate_temp_with_elif(20))