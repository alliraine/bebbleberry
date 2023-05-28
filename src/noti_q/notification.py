from pyray import load_texture


class Notification:
    def __init__(self, app, message, icon=load_texture(f"../res/icons/bell-solid.png"), time=400):
        self.app = app
        self.message = message
        self.icon = icon
