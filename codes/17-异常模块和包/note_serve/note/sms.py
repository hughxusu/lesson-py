from .base import Notification

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