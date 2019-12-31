name = 'Yvonne Bett'
NumberOfHoursWorkedInaWeek: int = 40
HourlyPayRate = 10
federal_tax_withholding_rate = 0.2
state_tax_withholding_rate = 0.9

GrossPay = HourlyPayRate * NumberOfHoursWorkedInaWeek
FederalTax = federal_tax_withholding_rate * GrossPay
StateTax = state_tax_withholding_rate * GrossPay
TotalDeductions = FederalTax + StateTax
netPay = GrossPay - TotalDeductions

print('Employees Full Name:', name)
print('Number of hours worked in a week:', NumberOfHoursWorkedInaWeek, 'hours')
print('Hourly Pay Rate: $', HourlyPayRate)
print('Gross Pay: $', GrossPay)
print('Federal Tax withholding (20%): $', FederalTax)
print('State Tax withholding rate (9%): $', StateTax)
print('Total Deductions:$', TotalDeductions)
print('Net Pay: $', netPay)




