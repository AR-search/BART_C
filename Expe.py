import random
import pandas as pd
import pygame.mixer
import main

# Initialize Pygame
pygame.init()

# Set the screen size and caption
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("BART")
screen_width, screen_height = screen.get_size()

# Load the background image
background_image = pygame.image.load("Img/Background_game.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# import variables from main.py
input_user = main.input_user
input_age = main.input_Age

# Load the image
original_image = pygame.image.load("Img/redBalloon.png")

# Set the initial size of the image
balloon_width = 100
balloon_height = 120

# Initialize the mixer
pygame.mixer.init()

# Load the burst sound
burst_sound = pygame.mixer.Sound("sounds/burst.wav")
cash_sound = pygame.mixer.Sound("Sounds/cash_S.mp3")

# Initialize the money counter
money = 0
Saved_money = 0
# Initialize the balloon inflated status
balloon_inflated = False

# Number of balloons
balloons_remaining = 20

# pump count
press_count = 0
# Burst chance
original_burst_chance = 0/116

# Money saved
Saved_money = 0
# Money for current balloon
money = 0

# Get the screen width and height
screen_width, screen_height = screen.get_size()

# Font for displaying money
font = pygame.font.SysFont("arial", 20)

# Store the results
results = pd.DataFrame(columns=["ID", "Age", "Trial", "Save_money", "Burst_chance", "Cash"])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                press_count += 1
                original_burst_chance = press_count / 116
                balloon_width += 2
                balloon_height += 2
                money += 1
                if not balloon_inflated:
                    balloon_inflated = True
                else:
                    # Check if the balloon burst
                    if random.random() < original_burst_chance:
                        balloons_remaining -= 1
                        balloon_width = 100
                        balloon_height = 120
                        # Play the burst sound
                        burst_sound.play()
                        # Reset money and pump count
                        money = 0
                        press_count = 0
                        # Append to the results data frame with the current burst chance
                        results = results.append({'ID': input_user, 'Age':input_age, 'Trial': balloons_remaining, 'Save_money': Saved_money, 'Burst_chance': original_burst_chance, "Cash": False}, ignore_index=True)
                        # Reset the burst chance
                        original_burst_chance = 0
                        # Set up the balloon
                        balloon_inflated = False
                        if balloons_remaining == 0:
                            running = False
            elif event.key == pygame.K_RETURN:
                balloons_remaining -= 1
                balloon_width = 100
                balloon_height = 120
                # Play the cash sound
                cash_sound.play()
                # Increment the saved money counter then reset the money counter and pump counter
                Saved_money += money
                money = 0
                press_count = 0
                # Append to the results data frame with the current burst chance
                results = results.append({'ID': input_user, 'Age':input_age, 'Trial': balloons_remaining, 'Save_money': Saved_money, 'Burst_chance': original_burst_chance, "Cash": True}, ignore_index=True)
                # Reset the burst chance
                original_burst_chance = 0
                if balloons_remaining == 0:
                    running = False


    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Create the data frame and write to Excel
    results.to_excel("Data/" + input_user + '.xlsx', index=False)

    # Scale the image to the new size
    image = pygame.transform.scale(original_image, (balloon_width, balloon_height))
    # Calculate the x and y positions to center the image
    x_pos = (screen_width - balloon_width) // 2
    y_pos = (screen_height - balloon_height) // 2 + 75
    # Draw the image on the screen
    screen.blit(image, (x_pos, y_pos))

    # Render the money counter
    money_text = font.render("Money: $" + str(money), True, (255, 255, 255))
    # Get the rect of the text
    money_rect = money_text.get_rect()
    # Position the rect in top right corner
    money_rect.topright = (screen_width - 10, 10)
    # Blit the text to the screen
    screen.blit(money_text, money_rect)

    # Render the Saved money counter
    Saved_money_text = font.render("Saved money: $" + str(Saved_money), True, (255, 255, 255))
    # Get the rect of the text
    Saved_money_rect = Saved_money_text.get_rect()
    # Position on top right corner
    Saved_money_rect.topright = (screen_width - 10, money_rect.bottom + 5)
    # Blit the text to the screen
    screen.blit(Saved_money_text, Saved_money_rect)

    # # Render the remaining balloons counter
    # balloons_remaining_text = font.render("Balloons Remaining: " + str(balloons_remaining), True, (255, 255, 255))
    # # Get the rect of the text
    # balloons_remaining_rect = balloons_remaining_text.get_rect()
    # # Position the rect in top left corner
    # balloons_remaining_rect.topleft = (10, 10)
    # # Blit the text to the screen
    # screen.blit(balloons_remaining_text, balloons_remaining_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
