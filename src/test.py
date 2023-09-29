import curses

def main(stdscr):
    # Clear screen
    curses.curs_set(False)
    stdscr.clear()

    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
    stdscr.addstr("hello\n")
        

    stdscr.refresh()
    stdscr.getkey()
    

curses.wrapper(main)



