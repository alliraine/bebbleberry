from pyray import *

s_width = 400
s_height = 240

def main():
    init_window(s_width, s_height, "Hello")
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_rectangle(0,0,s_width,20,BLACK)
        draw_text("New Message From Ellie!", 8, 3, 14, WHITE)
        end_drawing()
    close_window()


if __name__ == "__main__":
    main()
