from .base import Notification

class WXNotification(Notification):
    def __init__(self, user, account_balance, monthly_bill, wxid):
        super().__init__(user, account_balance, monthly_bill)
        self.wxid = wxid

    def send(self):
        print(f'调用【微信】api接口向{self.wxid}推送消息 📱')
        print('-' * 50)
        msg = self.get_note()
        print(msg)