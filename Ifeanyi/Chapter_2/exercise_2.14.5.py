principal_amount = input('what is Principal amount: ')

print('interest rate is 1%')
annual_nominal_interest_rate  = 1

number_of_times_the_interest_rate_is_compunded_per_year = input('enter the number of times the interest rate is compounded per year: ')

number_of_years = input('enter the number of years: ')

A= float(int(annual_nominal_interest_rate )/int(number_of_times_the_interest_rate_is_compunded_per_year))+1

B= int(number_of_times_the_interest_rate_is_compunded_per_year)*int(number_of_years)

final_amount = int(principal_amount)*(A**B)

print('The final_amount is ', final_amount)
