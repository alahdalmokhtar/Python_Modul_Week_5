from rectangel import  Rectangel


def main():
    rect=Rectangel(10,11)
    rect1=Rectangel(12,3)
    print("permiter is :",Rectangel.permiter(rect))
    print("area is :",Rectangel.area(rect))
    print("area is ",Rectangel.area(rect1))


if __name__==main():
    main()