from window import Window, Point, Line

def main():
    win = Window(800, 600)
    point1 = Point(25, 25)
    point2 = Point(200, 200)
    p3 = Point(25, 200)
    p4 = Point(200, 25)
    line2 = Line(p3, p4)
    line1 = Line(point1, point2)

    win.draw_line(line1, "red")
    win.draw_line(line2, "green")
    win.wait_for_close()

main()