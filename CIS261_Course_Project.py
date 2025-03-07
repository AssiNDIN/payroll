"""
Name :  N'din Assi 
Course: CIS 216 
Course name: Object Oriented Programming 1. 

"""

print("Welcome to Payrol system") 
"""This program automates the payrol system 
"""
print("Developed by Assi")

def main():
    number_of_employees=0
    total_hourss=0
    total_gross_pay=0 
    total_net_pay=0
    total_tax=0
    program_terminator="start"
    while program_terminator !="end": 
        
        program_terminator = input(" Do you wish to add another employee?").lower()
        #taking user input and changing it to lowercase, I should implement exception for handling integer entry
        if program_terminator=="end":
            break 
        
        employeename=employeeName()
        total_hours= totalHours()
        hourly_rates=hourlyRates()
        income_tax=incomeTax()
        grosspay,income_tax,net_pay=grossPay(total_hours,hourly_rates,income_tax)
        displayInfo(employeename,total_hours,hourly_rates,grosspay,income_tax,net_pay)
        number_of_employees= number_of_employees +1 
        total_hourss=total_hours+total_hours
        total_gross_pay=total_gross_pay + grosspay 
        total_net_pay=total_net_pay+net_pay
        total_tax= total_tax+income_tax
        summary(number_of_employees,total_hourss, total_gross_pay,total_tax,total_net_pay)
   
    
    
def employeeName():
    employee = input("Enter Employee name: ").capitalize()
    
    return employee

def totalHours():
    total_hours= float(input("Enter number of hours worked:  " ))
    return total_hours
def hourlyRates():
    hourly_rates= float(input("Enter hourly rates: "))
    return hourly_rates
def incomeTax():
    income_tax=float(input("Enter IncomeTax: "))
    return income_tax

def grossPay(total_hours,hourly_rates,tax_rate):
    
    grosspay= total_hours *hourly_rates
    income_tax=grosspay*tax_rate
    net_pay = grosspay-income_tax
    
    return grosspay,income_tax,net_pay

def displayInfo(employeename,totalhours,hourlyrates,grosspay,incometax,netpay):
    print("--------------------------")
    print("Added Employee information ")
    print(f"Employee Name: {employeename}")
    print(f"Total Hours: {totalhours}")
    print(f"Hourly rates: {hourlyrates}")
    print(f"Gross pay:  {grosspay}")
    print(f"Income Tax: {incometax}")
    print(f" Net Pay: {netpay} ")
    print("------------------------------")
    
def summary(number_of_employees,total_hours, total_gross,total_tax,total_net):
    print("--------------------------")
    print("PAYROL SUMMARY")
    print("----------------------------")
    print(f"Number of Employees: {number_of_employees}")
    print(f"Total Hours: {total_hours}")
    print(f"Total gross: {total_gross} ")
    print(f"Total pay:  {total_tax}")
    print(f"Total Net: {total_net}")
    print("----------------------------")
    
    

   
   
    
    
if __name__=="__main__":
    main()

    
                  

    
