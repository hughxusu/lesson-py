from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, user, account_balance, monthly_bill):
        self.user = user
        self.account_balance = account_balance
        self.monthly_bill = monthly_bill

    def calculate_new_balance(self):
        return self.account_balance - self.monthly_bill

    def get_note(self):
        new_balance = self.calculate_new_balance()
        if new_balance < 0:
            return f'亲爱的用户{self.user}，截止上月底，您已欠费：{new_balance:.2f}元，请及时充值。'
        else:
            return f'亲爱的用户{self.user}，截止上月底，您的账户余额为：{self.calculate_new_balance():.2f}元。'

    @abstractmethod
    def send(self):
        pass