# Enter your code here. Read input from STDIN. Print output to STDOUT
def check_bill_payment(money_brought, bill_amount):
    return "YES" if money_brought >= bill_amount else "NO"

# Read input
x, y = map(int, input().split())

# Print result
print(check_bill_payment(x, y))
