def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def convert_arr(arr):
    converted_arr = []
    for i in arr:
        if isfloat(i):
            converted_arr.append(float(i))
        else:
            try:
                converted_arr.append(complex(i))
            except:
                converted_arr.append(0)
    return (converted_arr)

def complex_(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def multiplication(a, b):
    return a*b


def division(a, b):
    return a/b


def call_operation(a, b, sign):
    if sign == '+':
        return complex_(a, b)
    if sign == '-':
        return subtraction(a, b)
    if sign == '*':
        return multiplication(a, b)
    if sign == '/':
        return division(a, b)