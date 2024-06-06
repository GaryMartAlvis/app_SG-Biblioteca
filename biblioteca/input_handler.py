import curses

def get_input(stdscr, prompt, max_length=40):
    h, w = stdscr.getmaxyx()
    content_x = int(w * 0.2) + 1
    stdscr.addstr(0, content_x, prompt)
    stdscr.refresh()
    curses.echo()
    user_input = stdscr.getstr(1, content_x, max_length).decode("utf-8")
    curses.noecho()
    stdscr.clear()
    return user_input
