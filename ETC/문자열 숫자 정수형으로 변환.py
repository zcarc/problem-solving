
def to_int(str_number):

    decimal = 0
    for char in str_number:
        decimal = decimal * 10 + int(char)

    return decimal


print(to_int('028703'))
print(type(to_int('028703')))