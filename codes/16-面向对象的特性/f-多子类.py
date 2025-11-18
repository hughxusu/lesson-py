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

class Fund(Investment):
    def __init__(self, principal, years, management_fee, expected_return):
        super().__init__(principal, years)
        self.management_fee = management_fee   
        self.expected_return = expected_return 
    
    def calculate_return(self):
        net_return = self.expected_return - self.management_fee
        total = self.principal * (1 + net_return) ** self.years
        profit = total - self.principal
        return total, profit
    
    def show_info(self):
        print(f'本金：{self.principal}元，年限：{self.years}，管理费率：{self.management_fee*100:.2f}%，预期收益：{self.expected_return*100:.2f}%')


fixed = FixedDeposit(10000, 3, 0.05)
print('定期存款信息：')
fixed.show_info()
total, profit = fixed.calculate_return()
print(f'总金额：{total:.2f}元，利润：{profit:.2f}元')
print('='*50)
fund = Fund(10000, 3, 0.005, 0.08)
print('基金信息：')
fund.show_info()
total, profit = fund.calculate_return()
print(f'基金总金额：{total:.2f}元，利润：{profit:.2f}元')