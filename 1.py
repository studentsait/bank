import math
import datetime 

# the following function is for mortage 
def caculate_monthly_payment(principal, rate, term):
    monthly_rate = rate / (12 / 100)
    term_months = term * 12 
    payment = (monthly_rate * principal * math(1 + monthly_rate, term_months)) / (math(math.pow(1 + monthly_rate, term_months) -1))
    return payment

