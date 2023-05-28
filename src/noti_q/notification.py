class Notification:
    def __init__(self, app, priority, message, icon, time=400):
        self.app = app
        self.priority = priority
        self.message = message
        self.icon = icon
        self.time = time

