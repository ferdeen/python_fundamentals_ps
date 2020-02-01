"""keypress from different os systems using try.  A module for detecting a single keypress."""

try:
    import msvcrt

    def getKey():
        """Wait for a keypress and return a single charater string."""
        return msvcrt.getch()

except ImportError:

    import sys 
    import tty
    import termios

    def getKey():
        """Wait for a keypress and return a single charater string."""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

        # if either of unix specific tty or termios are not  found allow error to propogate.