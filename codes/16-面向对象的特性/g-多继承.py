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

class PortfolioInvestment(FixedDeposit, Fund):
    """组合投资 - 多重继承：定期存款 + 基金"""
    def __init__(self, principal, years, fixed_ratio, fixed_rate, fund_management_fee, fund_expected_return):
        # 计算各部分本金
        self.fixed_principal = principal * fixed_ratio
        self.fund_principal = principal * (1 - fixed_ratio)
        
        # 分别调用两个父类的初始化方法
        FixedDeposit.__init__(self, self.fixed_principal, years, fixed_rate)
        Fund.__init__(self, self.fund_principal, years, fund_management_fee, fund_expected_return)
        
        # 组合投资特有属性
        self.total_principal = principal
        self.fixed_ratio = fixed_ratio
        self.fund_ratio = 1 - fixed_ratio
    
    def calculate_return(self):
        """计算组合投资的总收益"""
        # 分别计算两部分收益
        fixed_total, fixed_profit = FixedDeposit.calculate_return(self)
        fund_total, fund_profit = Fund.calculate_return(self)
        
        # 合并总收益
        total_return = fixed_total + fund_total
        total_profit = fixed_profit + fund_profit
        
        return total_return, total_profit
    
    def show_info(self):
        """显示组合投资信息"""
        print(f"=== 组合投资信息 ===")
        print(f"总投资本金：{self.total_principal}元，投资年限：{self.years}年")
        print(f"\n资产配置：")
        print(f"  定期存款：{self.fixed_ratio*100:.1f}% ({self.fixed_principal:.2f}元)")
        print(f"  基金：{self.fund_ratio*100:.1f}% ({self.fund_principal:.2f}元)")
        print(f"\n定期存款部分：")
        FixedDeposit.show_info(self)
        print(f"基金部分：")
        Fund.show_info(self)
        
        # 计算并显示收益
        total, profit = self.calculate_return()
        print(f"\n收益预测：")
        print(f"  定期存款到期金额：{self.fixed_principal * (1 + self.rate) ** self.years:.2f}元")
        print(f"  基金预期金额：{self.fund_principal * (1 + self.expected_return - self.management_fee) ** self.years:.2f}元")
        print(f"  组合总金额：{total:.2f}元")
        print(f"  组合总收益：{profit:.2f}元")
        print(f"  组合年化收益率：{(profit/self.total_principal/self.years)*100:.2f}%")

# 使用示例
if __name__ == "__main__":
    # 创建组合投资：总投资10万元，5年，50%定期存款(利率3%)，50%基金(管理费1%，预期收益8%)
    portfolio = PortfolioInvestment(
        principal=100000,
        years=5,
        fixed_ratio=0.5,           # 50%定期存款
        fixed_rate=0.03,           # 3%年利率
        fund_management_fee=0.01,  # 1%管理费
        fund_expected_return=0.08  # 8%预期收益
    )
    
    print("组合投资演示：")
    portfolio.show_info()
    
    print("\n" + "="*50)
    print("单独计算各部分收益：")
    
    # 单独创建定期存款和基金进行比较
    fixed_deposit = FixedDeposit(50000, 5, 0.03)
    fund_alone = Fund(50000, 5, 0.01, 0.08)
    
    fixed_total, fixed_profit = fixed_deposit.calculate_return()
    fund_total, fund_profit = fund_alone.calculate_return()
    
    print(f"单独定期存款收益：{fixed_profit:.2f}元")
    print(f"单独基金收益：{fund_profit:.2f}元")
    print(f"单独投资总收益：{fixed_profit + fund_profit:.2f}元")