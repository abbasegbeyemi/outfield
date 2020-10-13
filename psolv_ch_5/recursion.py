import string
import turtle
from random import choice


def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


def removeWhite(s):
    if len(s) <= 1:
        return s if s in string.ascii_lowercase else ""
    else:
        fl = s[0] if s[0] in string.ascii_lowercase else ""
        return fl + removeWhite(s[1:])


def isPal(s):
    revs = reverse(s)
    return True if s == revs else False


def drawSpiral(inTurtle, lineLen):
    if lineLen > 0:
        inTurtle.forward(lineLen)
        inTurtle.left(45)
        drawSpiral(inTurtle, lineLen - 1)


angleChoices = list(range(20, 61, 20))
lengthChoices = list(range(5, 21, 5))


def tree(branchLen, t, ps):
    if branchLen <= 15:
        t.color("green")
    else:
        t.color("black")
    if ps <= 1:
        ps = 1
    if branchLen > 5:
        ang = choice(angleChoices)
        lens = choice(lengthChoices)
        print(f"Current angle is {ang}")
        t.pensize(ps)
        t.forward(branchLen)
        t.right(ang)
        tree(branchLen - lens, t, ps - 2)
        t.left(2 * ang)
        tree(branchLen - lens, t, ps - 2)
        t.right(ang)
        t.backward(branchLen)


# Sierpinski Triangle
def drawTriangle(points, color, turt):
    turt.fillcolor(color)
    turt.up()
    turt.goto(points[0][0], points[0][1])
    turt.down()
    turt.begin_fill()
    turt.goto(points[1][0], points[1][1])
    turt.goto(points[2][0], points[2][1])
    turt.goto(points[0][0], points[0][1])
    turt.end_fill()


def getMid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, turt):
    colors = ['blue', 'green', 'violet', 'orange', 'yellow', 'red', 'black']
    drawTriangle(points, colors[degree], turt)

    if degree > 0:
        sierpinski(
            [
                points[0],
                getMid(points[0], points[1]),
                getMid(points[0], points[2])
            ],
            degree - 1, turt)
        sierpinski(
            [
                points[1],
                getMid(points[0], points[1]),
                getMid(points[1], points[2])
            ],
            degree - 1, turt)
        sierpinski(
            [
                points[2],
                getMid(points[2], points[1]),
                getMid(points[0], points[2])
            ],
            degree - 1, turt)


# Tower of Hanoi puzzle
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


def makeSerpinski():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-300, -250], [0, 100], [300, -250]]
    sierpinski(myPoints, 5, myTurtle)
    myWin.exitonclick()


if __name__ == '__main__':
    moveTower(5, "A", "C", "B")
