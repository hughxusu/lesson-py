class Investment:
    def __init__(self, principal, years):
        self.principal = principal
        self.years = years

class FixedDeposit(Investment):
    def __init__(self, principal, years):
        pass

fixed = FixedDeposit(10000, 3)
print(f'fixed.principal = {fixed.principal}')
