__author__ = 'zadjii'


class _Getch():
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except:
            self.impl = _GetchUnix()

    def __call__(self, *args, **kwargs):
        return self.impl()


class _GetchUnix():
    def __init__(self):
        import sys, tty

    def __call__(self, *args, **kwargs):
        import sys, tty, termios
        from fcntl import fcntl, F_SETFL, F_GETFL
        from os import O_NONBLOCK
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        # fcntl(sys.stdin, F_SETFL, fcntl(sys.stdin, F_GETFL) | O_NONBLOCK)


        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows():
    def __init__(self):
        import msvcrt

    def __call__(self, *args, **kwargs):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()


