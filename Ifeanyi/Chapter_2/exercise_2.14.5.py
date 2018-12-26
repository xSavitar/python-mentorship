'''This first 4 lines of code below takes input from the user.
First line is principal amount'''
Principal_amount = input('what is Principal amount: ')

'''Second is the annual nominal interest rate
which can be 1% or -0.05% '''
interest = input('interest: ')

'''Third line is yearly interest that is the number of times
the interest is compounded per year'''
yearly_interest = input('yearly interest: ')

'''Fourth line is for the number of years you want to calculate '''
years = input('enter the number of years: ')

''' "A" is the result of ratio of interest and yearly interest plus 1
float is use because the division might generate a decimal value
and interest can be in decimal'''
A= float(float(interest )/int(yearly_interest))+1

''' "B" is the result of product of yearly interest and years,
in this case no need of using float because product of
two integers is an integer'''
B= int(yearly_interest)*int(years)

'''Final amount is obtained by taken the "value of A" raised to the
power "B value" and multiplied by the principal amount'''
final_amount = int( Principal_amount)*(A**B)

'''This line of code is use to print the final amount'''
print('The final_amount is ', final_amount)
