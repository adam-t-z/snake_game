from turtle import Turtle  # Import the Turtle class for creating graphical elements
import random              # Import random module for generating random positions

class Food(Turtle):
    """
    Represents the food object in the game. The food is a small red circle that 
    appears at random locations on the screen for the snake to "eat."
    """

    def __init__(self):
        """
        Initializes the Food object by setting its shape, color, size, and position.
        Inherits from the Turtle class.
        """
        super().__init__()  # Call the Turtle class constructor
        self.shape("circle")  # Set the shape of the food to a circle
        self.color("red")  # Set the color of the food to red
        self.penup()  # Disable drawing while moving the food
        self.shapesize(0.5, 0.5)  # Adjust the food's size to make it smaller
        self.appear()  # Call the appear method to place the food at a random location

    def appear(self):
        """
        Moves the food to a random position on the screen. 
        The range is limited to fit within the game boundaries.
        """
        random_x = random.randint(-380, 380)  # Generate a random x-coordinate
        random_y = random.randint(-380, 380)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the new random location
