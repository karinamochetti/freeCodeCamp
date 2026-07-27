def get_loan_schedule(loan_amount, annual_rate, monthly_payment):
    rate = (annual_rate / 100) / 12
    
    arr = [float(loan_amount)]
    current = float(loan_amount)
    
    while current > 0:
        current = current + (current * rate) - monthly_payment
        if current < 0:
            current = 0
        arr.append(current)
        
    return [round(x) for x in arr]

print(get_loan_schedule(1000, 0, 200))
print(get_loan_schedule(1000, 5, 200))
print(get_loan_schedule(10, 50, 1))
print(get_loan_schedule(5500, 8, 400))
print(get_loan_schedule(50000, 5.2, 1650))
