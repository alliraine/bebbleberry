import logging
import os
import yaml
from pyray import *

s_width = 400
s_height = 240

selected = 0


def get_installed_apps():
    apps = []
    for app in [app for app in os.listdir("apps") if os.path.isdir(f"apps/{app}")]:
        with open(f"apps/{app}/manifest.yml", "r") as stream:
            try:
                manifest = yaml.safe_load(stream)
            except yaml.YAMLError:
                print(f"{app} does not have a manifest!! Aborting load")
        icon = load_texture(f"apps/{app}/res/launcher-icon.png")
        inverse_icon = load_texture(f"apps/{app}/res/launcher-icon-inverse.png")
        app = {
            "name": manifest["name"],
            "developer": manifest["developer"],
            "version": manifest["version"],
            "launch_file": manifest["launch_file"],
            "icon": icon,
            "inverse_icon": inverse_icon
        }
        apps.append(app)

    return apps


def main():
    global selected

    ## create emulation window
    init_window(s_width, s_height, "BebbleBerry Emulator")

    ## remove debug logs that spam
    # set_trace_log_level(logging.CRITICAL)

    ## loads apps from disk
    apps = get_installed_apps()

    while not window_should_close():

        # handle input. kinda hacky. I think I can do better
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

        # draw push notification
        draw_text("New Message From Ellie!", 8, 10, 10, WHITE)

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

            # set colors based on if selected
            bg_color = BLACK if i == selected else WHITE
            text_color = WHITE if i == selected else BLACK
            icon = app["inverse_icon"] if i == selected else app["icon"]

            # draw border
            draw_rectangle(app_x, app_y, 100, 100, BLACK)

            # draw background
            draw_rectangle(app_x + 5, app_y + 5, 90, 90, bg_color)

            # draw app name
            draw_text(app.get("name"), app_x + int((90 - (len(app.get("name") * 6))) / 2), app_y + 80, 14, text_color)

            # draw icon
            draw_texture(icon, app_x + 25, app_y + 15, text_color)

        end_drawing()
    close_window()


if __name__ == "__main__":
    main()
