from notification import Notification

class NotificationQueue:
    def __init__(self):
        self.queue = []

    def add_notification(self, notification: Notification):
        self.queue.append(notification)

    def get_noticication(self):
        if len(self.queue) > 0:
            print("next")