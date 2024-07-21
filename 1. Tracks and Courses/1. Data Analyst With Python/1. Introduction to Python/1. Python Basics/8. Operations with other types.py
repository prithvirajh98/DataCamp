'''
Exercise
Operations with other types
Hugo mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.

Instructions
100 XP
Calculate the product of monthly_savings and num_months. Store the result in year_savings.
What do you think the resulting type will be? Find out by printing out the type of year_savings.
Calculate the sum of intro and intro and store the result in a new variable doubleintro.
Print out doubleintro. Did you expect this?
'''

monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
year_savings = monthly_savings * num_months

# Print the type of year_savings
print(type(year_savings))

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)