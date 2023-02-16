paye = (30/100)
def kenyaPayAsYouEarnTax(grossSalary):
    tax = grossSalary * paye
    netPay = grossSalary - tax
    return netPay
userInput = int(input("Pleas enter your gross salary:"))
actualIncome = kenyaPayAsYouEarnTax(userInput)
print("Your actual salary is:", actualIncome)
