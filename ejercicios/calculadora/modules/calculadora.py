class Calculadora:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def res(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if b == 0:
            return "no puedes enviar un 0 de segundo parametro"
        return a / b



