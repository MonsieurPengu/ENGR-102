# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Ian Wang
# Section 510
# 227004716

# This code uses turtle to draw stuff.
from turtle import*


def upperleftcorner():  # This group moves the arrow to the upper left corner before it begins to draw the tallies.
    up()
    left(90)
    forward(300)
    left(90)
    forward(350)
    right(270)


def fiveblockone():  # This group draws 5 sets of 5 tallies into one line. You can call how many sets down below.
    block1 = 0
    while block1 <= 4:
        down()
        forward(100)
        up()
        left(90)
        forward(20)
        left(90)
        down()
        forward(100)
        up()
        right(90)
        forward(20)
        right(90)
        down()
        forward(100)
        up()
        left(90)
        forward(20)
        left(90)
        down()
        forward(100)
        up()
        back(100)
        left(30)
        down()
        forward(120)
        up()
        right(120)
        forward(110)
        right(90)
        forward(5)
        block1 += 1
        down()


def nextlinemover():  # This group moves the pen to the next line after maxing out at 5 sets in one line.
    up()
    forward(120)
    right(90)
    forward(551)
    left(90)


def tallymaker():  # This group is the tally maker: the master block: everything above is used here.
    tally = 0
    masterblock = 0
    upperleftcorner()
    usertally = int(input("How many sets? "))  # Asks the user how many sets aka rows of 25 they'd like.
    while masterblock != 4:  # I was trying to do a double loop but it just is a infinitely working parameter.
        while tally != usertally:  # Loop that allows the tallies to be drawn to the user's setting.
            fiveblockone()
            tally += 1
            masterblock += 1
            nextlinemover()


tallymaker()
input()
