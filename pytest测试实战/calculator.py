class Calaculator():
    def add(self, a, b):
        return a+b

    def subtrac(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        try:
            result = a/b
        except Exception as re:
            return re
        return result
