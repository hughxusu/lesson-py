class Notification:
    def __init__(self):
        pass
        
class EmailNotification(Notification):
    def __init__(self):
        super().__init__()
        pass
        
class SmsNotification(Notification):
    def __init__(self):
        super().__init__()
        pass

sms = SmsNotification()
print(f'sms is instance of Notification: {isinstance(sms, Notification)}')
print(f'sms is instance of EmailNotification: {isinstance(sms, EmailNotification)}')
print(f'sms is instance of SmsNotification: {isinstance(sms, SmsNotification)}')





