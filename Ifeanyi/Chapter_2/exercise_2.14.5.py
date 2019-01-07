'''First line is principal amount'''
Principal_amount = input('what is Principal amount: ')
'''The annual nominal interest rate which can be 1% or -0.05% '''
interest = input('interest: ')
'''yearly interest that is the number of times
the interest is compounded per year'''
yearly_interest = input('yearly interest: ')
'''The number of years you want to calculate '''
years = input('enter the number of years: ')
A = float(float(interest )/int(yearly_interest))+1
B = int(yearly_interest)*int(years)
'''Final amount is obtained by taken the "value of A" raised to the
power "B value" and multiplied by the principal amount'''
final_amount = int( Principal_amount)*(A**B)
print('The final_amount is ', final_amount)
