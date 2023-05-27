from pyray import *

s_width = 400
s_height = 240

selected = 0

apps = [
    {
        "name": "Beeper",
        "icon": 180,
    },
    {
        "name": "Settings",
        "icon": 141,
    },
    {
        "name": "Weather",
        "icon": 180,
    },
    {
        "name": "Email",
        "icon": 141,
    },
    {
        "name": "Beeper2",
        "icon": 180,
    },
    {
        "name": "Settings2",
        "icon": 141,
    },
    {
        "name": "Weather2",
        "icon": 180,
    },
    {
        "name": "Email2",
        "icon": 141,
    },
]


def main():
    global selected
    init_window(s_width, s_height, "Hello")
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
        draw_rectangle(0, 0, s_width, 20, BLACK)

        for app in apps:
            i = apps.index(app)
            a = 0
            if i > 0:
                a = 5
            app_x = 8 + (i * 100) - a * i
            app_y = 32
            if i > 3:
                app_y += 95
                x = i - 4
                app_x = 8 + (x * 100) - a * x

            # draw border
            draw_rectangle(app_x, app_y, 100, 100, BLACK)

            #set colors
            bg_color = WHITE
            text_color = BLACK
            if i == selected:
                bg_color = BLACK
                text_color = WHITE

            # draw background
            draw_rectangle(app_x + 5, app_y + 5, 90, 90, bg_color)

            # draw app name
            draw_text(app.get("name"),app_x + 10, app_y + 80, 14, text_color)

            gui_draw_icon(app.get("icon"), app_x + 25, app_y + 15, 3, text_color)

        # push notification
        draw_text("New Message From Ellie!", 8, 5, 10, WHITE)

        end_drawing()
    close_window()


if __name__ == "__main__":
    main()
