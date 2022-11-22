from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.pu()
        self.go_to_start()
        self.seth(90)


    def move_up(self):
        self.fd(10)

    #Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
    # When this happens, return the turtle to the starting position and increase the speed of the cars.
    # Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.
    def finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)


