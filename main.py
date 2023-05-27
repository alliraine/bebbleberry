import os

from pyray import *
from PIL import Image
import PIL.ImageOps

s_width = 400
s_height = 240

selected = 0

apps = [
    {
        "name": "Beeper",
        "icon": "cog-solid",
    },
    {
        "name": "BlueSky",
        "icon": "cloud-solid",
    },
    {
        "name": "Weather",
        "icon": "cloud-sun-rain-solid",
    },
    {
        "name": "Settings",
        "icon": "cog-solid",
    },
    {
        "name": "Calendar",
        "icon": "calendar-solid",
    },
    {
        "name": "Notes",
        "icon": "sticky-note-solid",
    },
    {
        "name": "Terminal",
        "icon": "terminal-solid",
    },
    {
        "name": "App Store",
        "icon": "download-solid",
    },
]


def main():
    global selected
    init_window(s_width, s_height, "BebbleBerry Emulator")

    # create inverse of all icons
    for file in os.listdir('icons'):
        file = file.split(".")[0]
        if "-inverse" not in file and file != "":
            img = Image.open(f'icons/{file}.png')
            r, g, b, a = img.split()
            def invert(image):
                return image.point(lambda p: 255 - p)
            r, g, b = map(invert, (r, g, b))
            img2 = Image.merge(img.mode, (r, g, b, a))

            img2.save(f'icons/{file}-inverse.png')

    while not window_should_close():
        # handle input
        if is_key_pressed(264) and selected + 4 < len(apps):
            selected += 4
        if is_key_pressed(265) and selected - 4 >= 0:
            selected -= 4
        if is_key_pressed(262) and selected + 1 < len(apps):
            selected += 1
        if is_key_pressed(263) and selected - 1 >= 0:
            selected -= 1

        begin_drawing()
        clear_background(WHITE)

        # draw notifications bar
        draw_rectangle(0, 0, s_width, 30, BLACK)

        for app in apps:

            ## TODO: Make all of this math for figure out the app x and y actually make sense. Also pagenate
            i = apps.index(app)
            a = 0
            if i > 0:
                a = 5
            app_x = 8 + (i * 100) - a * i
            app_y = 37

            # super hacky way to add a second row. cannot math to figure this one out right now
            if i > 3:
                app_y += 95
                x = i - 4
                app_x = 8 + (x * 100) - a * x

            # draw border
            draw_rectangle(app_x, app_y, 100, 100, BLACK)

            #set colors
            bg_color = WHITE
            text_color = BLACK
            icon = load_texture(f"icons/{app.get('icon')}.png")

            if i == selected:
                bg_color = BLACK
                text_color = WHITE
                icon = load_texture(f"icons/{app.get('icon')}-inverse.png")


            # draw background
            draw_rectangle(app_x + 5, app_y + 5, 90, 90, bg_color)

            # draw app name
            draw_text(app.get("name"),app_x + int((90 - (len(app.get("name") * 6))) / 2), app_y + 80, 14, text_color)

            draw_texture(icon, app_x + 25, app_y + 15, text_color)

        # push notification
        draw_text("New Message From Ellie!", 8, 10, 10, WHITE)

        end_drawing()
    close_window()


if __name__ == "__main__":
    main()
