def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        if int(str_number[1:]) != 0:
            prod = first * get_multiplied_digits(int(str_number[1:]))
            return prod
    else:
        return first

result = get_multiplied_digits(75033094)
print(result)