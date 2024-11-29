from turtle import Turtle  # Import the Turtle class for graphical objects

class Snake:
    """
    Represents the snake in the game. The snake is made up of square segments
    and can move, grow, and change direction based on user input.
    """

    def __init__(self):
        """
        Initializes the Snake object by creating its segments and setting the starting position.
        """
        self.turtles = []  # List to store the segments of the snake
        self.position = [(-40, 0), (-20, 0), (0, 0)]  # Initial positions of the snake's segments
        self.create_snake()  # Create the initial snake
        self.head = self.turtles[-1]  # The last segment is the snake's head

    def create_snake(self):
        """
        Creates the initial snake with three segments positioned horizontally.
        Each segment is a square with a specific color.
        """
        for i in range(len(self.position)):  # Loop through the initial positions
            new_turtle = Turtle("square")  # Create a new square segment
            new_turtle.color("chartreuse")  # Set the color of the segment
            new_turtle.penup()  # Prevent drawing while moving
            new_turtle.goto(self.position[i])  # Position the segment
            self.turtles.append(new_turtle)  # Add the segment to the list

    def move(self):
        """
        Moves the snake forward by updating the position of each segment.
        The last segment moves to the position of the one before it, except for the head.
        """
        for i in range(len(self.turtles) - 1):  # Move all segments except the head
            self.turtles[i].goto(self.turtles[i + 1].pos())  # Move each segment to the next one's position
        self.head.forward(20)  # Move the head forward by 20 pixels

    def extend(self):
        """
        Adds a new segment to the snake at the position of the tail.
        The snake grows in size each time this method is called.
        """
        new_segment = Turtle("square")  # Create a new square segment
        new_segment.color("chartreuse")  # Set the color to match the rest of the snake
        new_segment.penup()  # Prevent drawing while moving
        new_segment.goto(self.turtles[0].pos())  # Place the new segment at the tail's position
        self.turtles.insert(0, new_segment)  # Add the new segment to the beginning of the list

    def up(self):
        """
        Changes the snake's head direction to up (90 degrees).
        """
        self.head.setheading(90)

    def down(self):
        """
        Changes the snake's head direction to down (270 degrees).
        """
        self.head.setheading(270)

    def right(self):
        """
        Changes the snake's head direction to right (0 degrees).
        """
        self.head.setheading(0)

    def left(self):
        """
        Changes the snake's head direction to left (180 degrees).
        """
        self.head.setheading(180)
