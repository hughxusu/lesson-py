from note import email, sms, wx, serve
# from note import *
# from note import serve

email_note = email.EmailNotification('张三', 100, 84, 'zs@example.com')
sms_note = sms.SmsNotification('张三', 100, 84, '13800001234')
wx_note = wx.WXNotification('张三', 100, 84, 'zs-wx')

service = serve.NotificationService()
service.add_notification(email_note)
service.add_notification(sms_note)
service.add_notification(wx_note)

service.send_all()
