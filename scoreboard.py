from turtle import Turtle  # Import the Turtle class to create the scoreboard

class Scoreboard(Turtle):
    """
    Represents the scoreboard in the game.
    Tracks and displays the player's score and shows a game-over message when the game ends.
    """

    def __init__(self):
        """
        Initializes the scoreboard with a starting score of 0 and positions it at the top center of the screen.
        Inherits from the Turtle class.
        """
        super().__init__()  # Call the Turtle class constructor
        self.score = 0  # Initialize the score to 0
        self.color("white")  # Set the text color to white
        self.penup()  # Disable drawing when moving the turtle
        self.goto(0, 350)  # Position the scoreboard at the top center of the screen
        self.hideturtle()  # Hide the turtle shape (only the text will be visible)
        self.update_scoreboard()  # Display the initial score

    def update_scoreboard(self):
        """
        Displays the current score on the screen.
        Clears any previous text before writing the updated score.
        """
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """
        Increments the score by 1 and updates the scoreboard display.
        """
        self.score += 1  # Increase the score
        self.clear()  # Clear the previous score display
        self.update_scoreboard()  # Write the updated score

    def game_over(self):
        """
        Changes the background to a "game-over" theme and displays a final score message.
        """
        self.screen.bgcolor("darkred")  # Change the screen background color to dark red
        self.goto(0, 0)  # Move the text to the center of the screen
        self.write(f"  Game Over \nFinal Score: {self.score}", align="center", font=("Arial", 24, "normal"))
