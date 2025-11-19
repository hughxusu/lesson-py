from base import Notification

class EmailNotification(Notification):
    def __init__(self, user, account_balance, monthly_bill, email):
        super().__init__(user, account_balance, monthly_bill)
        self.email = email

    def send(self):
        print(f'调用【邮箱】api接口向{self.email}发送 📧')
        print('-'*50)
        msg = f'用户，您好：\n'
        msg += self.get_note()
        msg += f'\n\n'
        msg += ' ' * 36
        msg += '【中国联通】'
        print(msg)
