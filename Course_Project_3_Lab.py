#Suraya Malek
#CIS261

from xml.dom.minicompat import EmptyNodeList


def getEmpName():
    empname = input("Enter employee name: ")
    return empname

def getDatesWorked():
    fromdate = input("Enter start date (mm/dd/yyyy): ")
    todate = input("Enter End date (mm/dd/yyyy): ")
    return fromdate, todate

def getHoursWorked():
    hours = float( input ("Enter amount of hours worked: "))
    return hours

def getHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def getTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for Emplist in EmpDetailList:
        fromdate = Emplist[0]
        todate - Emplist[1]
        empname = Emplist[2]
        hours = Emplist[3]
        hourlyrate =Emplist[4]
        taxrate = Emplist[5]
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,. 2f}", f"{hourlyrate:,. 2f}", f"{grosspay:,. 2f}", f"{taxrate:,. 1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TOtNetPay"] = TotNetPay
        
def PrintTotals(EmpTotals):
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total Hours Worked: {EmpTotals['TotHrs']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total Income Tax: {EmpTotals['TotTax']:,.1%}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")
    
def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")
    
    file.write('{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def getFromDate():
    valid = False
    fromdate = ""
    
    while not valid:
        fromdate = input("Enter From Date (mm/dd/yyyy): ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid Date Format: ")
        else:
            valid = True
    
    return fromdate

def ReadEmployeeInformation(fromdate):
    EmpDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    condition = True
    
    if fromdate.upper() == 'ALL':
        condition = False
     
    for employee in data:

        employee = [x.stri() for x in employee .strip().split("|")]
        
    if not condition:
        EmpDetailList.append(
            [employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])

    return EmpDetailList

if __name__ == "__main__":
   EmpDetailList = []
   EmpTotals = {}
   
   while True:
       empname = getEmpName()
       if (empname.upper() == "END"):
           break 
       
       fromdate, todate = getDatesWorked()
       hours = getHoursWorked()
       hourlyrate = getHourlyRate()
       taxrate = getTaxRate()
       
       print()
       
       EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
       WriteEmployeeInformation(EmpDetail)
       
   print()
   print()
   fromdate = getFromDate()
   EmpDetailList - ReadEmployeeInformation(fromdate)
   
   print()
   printinfo(EmpDetailList)
 
print()
PrintTotals(EmpTotals)