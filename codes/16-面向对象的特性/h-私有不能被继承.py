class Investment:
    def __init__(self, principal, years):
        self.__principal = principal
        self.__years = years

    def __show_info(self):
        print(f'本金：{self.principal}元，年限：{self.years}')

class FixedDeposit(Investment):
    def __init__(self, principal, years):
        super().__init__(principal, years)

fixed = FixedDeposit(10000, 3)
print(f'本金：{fixed.__principal}元，年限：{fixed.__years}')

# fixed.__show_info()
