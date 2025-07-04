from turtle import *
import time

for _ in range(5):
    forward(10)
    time.sleep(1)

    penup()
    time.sleep(1)

    forward(6)
    time.sleep(1)

    pendown()
    time.sleep(1)

turtle.done()
