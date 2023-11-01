from rectangle import Rectangle


def main():
    rec = Rectangle(0, 1, 1, 0)
    rec1 = Rectangle(5, 3, 3, 5)  # rec1 next to rec - does not contain and does not intersect
    rec2 = Rectangle(0.2, 0.7, 0.7, 0.2)  # rec2 in rec - rec contains rec2
    rec3 = Rectangle(-1, 2, 2, -1)  # rec in rec3 - rec3 contains rec
    rec4 = Rectangle(-3, 3, 0.5, -1)  # rec4 intersects rec
    rec5 = Rectangle(0.5, 2, 2, 0.5)  # rec5 intersects rec

    print(Rectangle.contains(rec, rec1))
    print(Rectangle.contains(rec, rec2))
    print(Rectangle.contains(rec, rec3))
    print(Rectangle.intersect(rec, rec1))
    print(Rectangle.intersect(rec, rec4))
    print(Rectangle.intersect(rec, rec5))


if __name__ == "__main__":
    main()
