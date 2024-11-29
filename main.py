# Import necessary modules
from turtle import Turtle, Screen  # Turtle and Screen classes for the GUI
from snake import Snake           # Snake class for handling the snake behavior
from food import Food             # Food class for managing the food object
from scoreboard import Scoreboard # Scoreboard class for tracking the score
import time                       # Time module for delay handling

# Set up the game screen
window = Screen()  # Create a Screen object
window.setup(800, 800)  # Set up the window size to 800x800 pixels
window.bgcolor("black")  # Set the background color to black
window.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create game objects
snake = Snake()  # Initialize the Snake object
food = Food()  # Initialize the Food object
score = Scoreboard()  # Initialize the Scoreboard object

# Start the game loop
game_on = True  # Boolean flag to control the game loop
while game_on:
    # Move the snake forward
    snake.move()

    # Pause the game briefly to control the speed
    time.sleep(0.1)

    # Update the screen to show the latest changes
    window.update()

    # Listen for keypress events to control the snake
    window.listen()
    window.onkey(snake.up, "Up")      # Move the snake up when the "Up" key is pressed
    window.onkey(snake.down, "Down")  # Move the snake down when the "Down" key is pressed
    window.onkey(snake.right, "Right") # Move the snake right when the "Right" key is pressed
    window.onkey(snake.left, "Left")   # Move the snake left when the "Left" key is pressed

    # Check if the snake eats the food
    if snake.head.distance(food) < 15:  # If the snake's head is close to the food
        food.appear()                   # Move the food to a random new location
        snake.extend()                  # Extend the snake's length
        score.increase_score()          # Increase the score

    # Check for collision with walls
    if (snake.head.xcor() > 370 or  # If the snake's head goes beyond the right boundary
        snake.head.xcor() < -370 or # If the snake's head goes beyond the left boundary
        snake.head.ycor() > 370 or  # If the snake's head goes beyond the top boundary
        snake.head.ycor() < -370):  # If the snake's head goes beyond the bottom boundary
        game_on = False             # End the game
        score.game_over()           # Display the "Game Over" message

    # Check for collision with the snake's own body
    for segment in snake.turtles[:-1]:  # Loop through all segments except the head
        if snake.head.distance(segment) < 15:  # If the head touches any segment
            game_on = False                   # End the game
            score.game_over()                 # Display the "Game Over" message
            break                             # Exit the loop to avoid multiple triggers

# Close the window when clicked
window.exitonclick()
