import math

def monthlypayment(princ, rate, time):
    m = princ * rate / (1 - math.pow(1 + rate, - time))
    return m

