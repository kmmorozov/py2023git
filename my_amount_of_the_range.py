def my_amount(a, b):
    amount = 0
    if a > b:
        for i in range(b, a + 1):
            amount = amount + i
        return amount
    else:
        for i in range(a, b + 1):
            amount = amount + i
        return amount
