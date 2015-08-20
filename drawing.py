__author__ = 'zadjii'
import sys


BLACK       = 0
RED         = 1
GREEN       = 2
YELLOW      = 3
BLUE        = 4
MAGENTA     = 5
CYAN        = 6
WHITE       = 7
CLEAR       = 9

FOREGROUND = 30
BACKGROUND = 40

BOLD = '5;'

ESC = '\x1b['

def clear_color_sequence():
    return ESC+'0m'


def get_fg_sequence(color):
    return ESC+str(color+FOREGROUND)+'m'


def get_bg_sequence(color):
    return ESC+str(color+BACKGROUND)+'m'


def get_fg_bold_sequence(color):
    return ESC+BOLD+str(color+FOREGROUND)+'m'


def get_bg_bold_sequence(color):
    # I kinda doubt this actually works...
    return ESC+BOLD+str(color+BACKGROUND)+'m'

def clear_screen_sequence():
    return ESC+'2J'

def move_to_sequence(x, y):
    # return ESC+str(y+1)+';'+str(x+1)+'H'
    return ESC+str(x+1)+';'+str(y+1)+'f'


def reset_sequence():
    return clear_color_sequence() \
           + clear_screen_sequence() \
           + move_to_sequence(0,0) \

def do_reset():
    reset = reset_sequence()
    sys.stdout.write(reset)
    # sys.stdout.flush()

def do_move(x, y):
    sys.stdout.write(move_to_sequence(x, y))
    # sys.stdout.flush()


def fg_brush(color):
    sys.stdout.write(get_fg_sequence(color))
    # sys.stdout.flush()


def bg_brush(color):
    sys.stdout.write(get_bg_sequence(color))
    # sys.stdout.flush()


def render_cell(fg, bg0, bg1):
    fg_char = None
    fg_color = None
    bg_color = None
    if ( fg[0] is ' ') or ( fg[0] is None):
        if (bg0[0] is ' ') or (bg0[0] is None):
            if (bg1[0] is ' ') or (bg1[0] is None):
                fg_char = ' '
                fg_color = CLEAR
            else:
                fg_char = bg1[0]
                fg_color = bg1[1]
        else:
            fg_char = bg0[0]
            fg_color = bg0[1]
    else:
        fg_char = fg[0]
        fg_color = fg[1]
    if (fg[2] is CLEAR) or (fg[2] is None):
        if (bg0[2] is CLEAR) or (bg0[2] is None):
            if (bg1[2] is CLEAR) or (bg1[2] is None):
                bg_color = CLEAR
            else:
                bg_color = bg1[2]
        else:
            bg_color = bg0[2]
    else:
        bg_color = fg[2]
    fg_brush(fg_color)
    bg_brush(bg_color)
    sys.stdout.write(fg_char)
    # print(fg_char)
    sys.stdout.flush()
