class NotificationService:
    def __init__(self):
        self.notes = []

    def add_notification(self, note):
        self.notes.append(note)

    def send_all(self):
        print('=' * 50)
        for note in self.notes:
            note.send()
            print('=' * 50)