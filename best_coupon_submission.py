def calculate_max_discount(bill_amount):
    percent_discount = bill_amount * 0.1
    flat_discount = 100
    return bill_amount - max(percent_discount, flat_discount)
bill = int(input())
print(int(calculate_max_discount(bill)))
