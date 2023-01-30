import pygame

# Initialize pygame
pygame.init()

# Set the screen size
size = (640, 480)
screen = pygame.display.set_mode(size)
screen_width, screen_height = screen.get_size()

# Set the title of the screen
pygame.display.set_caption("BART")

# Load the background image
background_image = pygame.image.load("Img/Background_game.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load the image for the start button
start_image = pygame.image.load("Img/Start_button.png")
scaled_start_image = pygame.transform.scale(start_image, (100, 50))
start_rect = scaled_start_image.get_rect()
start_rect.center = (size[0]/2, size[1]/2 + 100)

# Create the text for the button
button_font = pygame.font.SysFont("arial", 20)
start_text = button_font.render("Start", True, (255, 255, 255))
text_center = (start_text.get_rect().width/2, start_text.get_rect().height/2)

# Create input text box
input_box = pygame.Rect(size[0]/2-150, size[1]/2-50, 300, 30)
input_box_active = False
input_font = pygame.font.SysFont("arial", 20)

# Create input text box for age
input_Age_box = pygame.Rect(size[0]/2-150, size[1]/2+0, 300, 30)
input_Age_active = False

# variable to store user input
input_user = "user"
input_Age = "age"

# create a cross Image

cross_image = pygame.image.load("Img/cross.png")
scaled_cross_image = pygame.transform.scale(cross_image, (50, 50))
cross_rect = scaled_cross_image.get_rect()
cross_rect.topright = (size[0]-10, 10)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(mouse_pos):
                exec(open("Expe.py").read())
                running = False
            elif cross_rect.collidepoint(mouse_pos):
                running = False
                pygame.quit()
            elif input_box.collidepoint(mouse_pos):
                input_box_active = True
                input_Age_active = False
            elif input_Age_box.collidepoint(mouse_pos):
                input_Age_active = True
                input_box_active = False
            else:
                input_box_active = False
                input_Age_active = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if input_box_active:
                    input_user = input_user[:-1]
                elif input_Age_active:
                    input_Age = input_Age[:-1]
            elif event.key == pygame.K_RETURN:
                exec(open("Expe.py").read())
                running = False
            else:
                if event.unicode.isalpha() or event.unicode.isdigit():
                    if input_box_active:
                        input_user += event.unicode
                    elif input_Age_active:
                        input_Age += event.unicode

    # Draw the button on the screen
    screen.fill((0, 0, 0))
    # Draw the background image
    screen.blit(background_image, (0, 0))
    # Display start button
    screen.blit(scaled_start_image, start_rect)
    screen.blit(start_text, (start_rect.centerx - text_center[0], start_rect.centery - text_center[1]))
    # Draw the input box
    pygame.draw.rect(screen, (255, 255, 255), input_box)
    input_text = input_font.render(input_user, True, (0, 0, 0))
    screen.blit(input_text, (input_box.x + 5, input_box.y + 5))
    # Draw the input box for age
    pygame.draw.rect(screen, (255, 255, 255), input_Age_box)
    input_Age_text = input_font.render(input_Age, True, (0, 0, 0))
    screen.blit(input_Age_text, (input_Age_box.x + 5, input_Age_box.y + 5))
    # draw the cross
    screen.blit(scaled_cross_image, cross_rect)

    pygame.display.flip()

# Quit pygame
pygame.quit()
