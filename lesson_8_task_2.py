class Div_to_0:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_to_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Devide to '0' is impossible")


div = Div_to_0(10, 100)
print(Div_to_0.divide_to_null(10, 0))
print(Div_to_0.divide_to_null(10, 0.1))
print(div.divide_to_null(100, 0))
