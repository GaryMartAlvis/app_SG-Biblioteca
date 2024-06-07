def draw_content(stdscr, content):
    h, w = stdscr.getmaxyx()
    content_x = int(w * 0.2) + 1
    offset = 0  

    for idx, row in enumerate(content):
        stdscr.addstr(idx + offset, content_x, row[:w - content_x - 1])
    stdscr.refresh()
