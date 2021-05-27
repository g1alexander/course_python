"""

    Twitter: @g1_alexander

"""


def sum(a, b):
    return a + b


def res(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "no puedes enviar un 0 de segundo parametro"
    return a / b


print(sum(4, 5))
print(res(4, 5))
print(mul(4, 5))
print(div(4, 4))
