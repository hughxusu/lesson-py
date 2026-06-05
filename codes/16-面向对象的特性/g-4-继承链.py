class Notification:
    def __init__(self):
        self.name = 'Notification'
        print('Notification __init__')
        
class EmailNotification(Notification):
    def __init__(self):
        super().__init__()
        self.name = 'EmailNotification'
        print('EmailNotification __init__')
        
class SmsNotification(Notification):
    def __init__(self):
        super().__init__()
        self.name = 'SmsNotification'
        print('SmsNotification __init__')
        
class MultiChannelNotifier(EmailNotification, SmsNotification):
    def __init__(self):
        super().__init__()
        self.name = 'MultiChannelNotifier'
        print('MultiChannelNotifier __init__')
        
note = MultiChannelNotifier()
print(MultiChannelNotifier.__mro__)
print(note.name)



