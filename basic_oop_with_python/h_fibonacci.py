def fibonacci(i):  # this function will calculate the first 20 fibonacci numbers.
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i-1) + fibonacci(i-2)
