#Program to calculate compound interest with formula as given by Wikipedia

print("Input the following parameters to calculate final amount for compound interest\n")

initInvestment = int(input("Initial investment: "))
rate = float(input("rate(%): "))
frequency =int(input("Number of times interest is compounded per year: "))
num_of_yrs =int(input ("Number of years interest is calculated for: "))

finalAmt =int(initInvestment * ((1 + float(rate / (100 * frequency))) ** (frequency * num_of_yrs)))

print("Final amount is" ,finalAmt)
