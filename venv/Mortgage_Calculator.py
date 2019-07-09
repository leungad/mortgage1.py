
present = input('Please enter PV: ')
int_present = int(present)

rate = input('Please enter rate: ')
float_rate = float(rate)

period = input('Please enter period length: ')
int_period = int(period)

cashflow = int_present /((1/float_rate) * (1-((1/(1+float_rate)**int_period))))


print('Your monthly mortgage payment is $' + '{0:.2f}'.format(cashflow) + ' dollars.')