import curses

def draw_menu(stdscr, menu, current_row_idx):
    h, w = stdscr.getmaxyx()
    menu_width = int(w * 0.2)
    for idx, row in enumerate(menu):
        x = 0
        y = idx
        if idx == current_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row[:menu_width])
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row[:menu_width])
    stdscr.refresh()
