# Define the function
def add_three(input_var):
    output_var = input_var + 3
    return output_var

new_number = add_three(10)
print(new_number)

def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

# Calculate pay based on working 40 hours
pay_fulltime = get_pay(40)
print(pay_fulltime)

pay_parttime = get_pay(32)
print(pay_parttime)

#Multiple Arguements Defined
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax

#Call veriable with inputs
higher_pay_aftertax = get_pay_with_more_inputs(40, 24, .22)
print(higher_pay_aftertax)

same_pay_fulltime = get_pay_with_more_inputs(40, 15, .12)
print(same_pay_fulltime)

# Define the function with no arguments and with no return
def print_hello():
    print("Hello, you!")
    print("Good morning!")
    
# Call the function
print_hello()