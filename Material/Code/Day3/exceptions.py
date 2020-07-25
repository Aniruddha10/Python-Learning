
def divide(dividend, divisor):
    if divisor == 0:
        raise FileNotFoundError("cannot divide by zero")
    return dividend/divisor


try:
    print(divide(5, 0))
except FileNotFoundError as e:
    print(e)
