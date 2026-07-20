class Investment:
    def __init__(self, principal, years):
        self.__principal = principal
        self.__years = years

class FixedDeposit(Investment):
    def __init__(self, principal, years):
        super().__init__(principal, years)

    def __str__(self):
        return f'定期存款：本金{self.__principal}元，年限{self.__years}年'

fixed = FixedDeposit(10000, 3)
print(fixed)
