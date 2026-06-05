class Investment:
    def __init__(self, principal, years):
        self.principal = principal
        self.years = years

    def show_info(self):
        print(f'本金：{self.principal}元，年限：{self.years}')

class FixedDeposit(Investment):
    def __init__(self, principal, years):
        super().__init__(principal, years)

fixed = FixedDeposit(10000, 3)
fixed.show_info()
