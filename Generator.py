def even_numbers(n):
    for number in range(0, n + 1):
        if number % 2 == 0:
            yield number


for num in even_numbers(10):
    print(num)