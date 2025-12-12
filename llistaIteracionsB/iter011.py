def divideix(dividend, divisor):
    if dividend < divisor:
        return 0
    else:
        return 1 + divideix(dividend - divisor, divisor)

def divideix2(dividend, divisor):
    if dividend < divisor:
        return 0, dividend
    else:
        d1, d2 = divideix2(dividend - divisor, divisor)
        return d1 + 1, d2

print(divideix2(12, 3))
print(divideix2(12, 4))
print(divideix2(12, 5))
print(divideix2(12, 6))
print(divideix2(12, 7))
print(divideix2(2, 7))