__author__ = 'zadjii'


BLACK       = 0
RED         = 1
GREEN       = 2
YELLOW      = 3
BLUE        = 4
MAGENTA     = 5
CYAN        = 6
WHITE       = 7

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
    return ESC+str(y)+';'+str(x)+'H'

def reset_sequence():
    return clear_color_sequence() \
           + move_to_sequence(0,0) \
           + clear_screen_sequence() \
