import random
import turtle
wn=turtle.Screen()
wn.addshape("12.gif")
wn.addshape("13.gif")
turtle.setup(800, 600)

    class Game():
        def __init__(self):
            self.score=0
            self.pointsDisplay=Points()
