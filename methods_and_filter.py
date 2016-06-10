def filter_numbers(test):
    data = []
    for n in range(0, 100):
        if test(n):
            data.append(n)

    return data


# def even(num):
#     return num % 2 == 0


d = filter_numbers(lambda num: num % 11 == 0)
print(d)