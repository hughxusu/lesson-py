class Investment(object):
    def __init__(self, principal, years):
        self.principal = principal
        self.years = years

    def show_info(self):
        print(f'本金：{self.principal}元，年限：{self.years}')

inv = Investment(10000, 3)
inv.show_info()
