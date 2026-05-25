class Investment:
    def __init__(self, principal, years):
        self.principal = principal
        self.years = years

    def show_info(self):
        print(f'本金：{self.principal}元，年限：{self.years}')

class FixedDeposit(Investment):
    def __init__(self, principal, years, rate):
        super().__init__(principal, years)
        self.rate = rate

    def calculate_return(self):
        # 复利计算：本金 * (1 + 利率)^年限
        total = self.principal * (1 + self.rate) ** self.years
        profit = total - self.principal
        return total, profit

    def show_info(self):
        print(f'本金：{self.principal}元，年限：{self.years}，利率：{self.rate}')

fixed = FixedDeposit(10000, 3, 0.05)
fixed.show_info()