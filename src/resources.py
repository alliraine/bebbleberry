from pyray import load_font, load_texture

from src.noti_q.noti_q import NotificationQueue


class ResourceManager:
    def __init__(self):
        self.s_width = 400
        self.s_height = 240

        self.noti_q = NotificationQueue()
        self.MukataBold = load_font("res/fonts/Mukta-Bold.ttf")
        self.MukataSemiBold = load_font("res/fonts/Mukta-SemiBold.ttf")
        self.MukataRegular = load_font("res/fonts/Mukta-Regular.ttf")

        self.bell = load_texture("res/icons/bell-solid.png")
        self.wifi = load_texture("res/icons/wifi-solid.png")
        self.bluetooth = load_texture("res/icons/bluetooth-brands.png")
        self.battery_level = [
            load_texture("res/icons/battery-empty-solid.png"),
            load_texture("res/icons/battery-quarter-solid.png"),
            load_texture("res/icons/battery-half-solid.png"),
            load_texture("res/icons/battery-full-solid.png")
        ]