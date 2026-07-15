class Notification:
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

class EmailNotification(Notification):
    def __init__(self, user, account_balance, monthly_bill, email):
        super().__init__(user, account_balance, monthly_bill)
        self.email = email

    def send(self):
        print(f'调用【邮箱】api接口向{self.email}发送 📧')
        print('-' * 50)
        msg = f'用户，您好：\n'
        msg += self.get_note()
        msg += f'\n\n'
        msg += ' ' * 36
        msg += '【中国联通】'
        print(msg)

class SmsNotification(Notification):
    def __init__(self, user, account_balance, monthly_bill, phone):
        super().__init__(user, account_balance, monthly_bill)
        self.phone = phone

    def send(self):
        print(f'调用【短信】api接口向{self.phone}发送短信 📱')
        print('-' * 50)
        msg = f'【中国联通】'
        msg += self.get_note()
        print(msg)

class MultiChannelNotifier(EmailNotification, SmsNotification):
    def __init__(self, user, account_balance, monthly_bill, email, phone):
        Notification.__init__(self, user, account_balance, monthly_bill)
        self.email = email
        self.phone = phone

    def send(self):
        print('=' * 50)
        EmailNotification.send(self)
        print('=' * 50)
        SmsNotification.send(self)
        print('=' * 50)

d = MultiChannelNotifier('李四', 100, 128, 'zhangsan@example.com', '13800001234')
d.send()



