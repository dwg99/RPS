import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set the window size and caption
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rock Paper Scissors')

# Set the font
font = pygame.font.Font(None, 32)

# Define the button sizes and positions
button_width, button_height = 200, 50
button_x, button_y = (screen_width - button_width) // 2, (screen_height - 3 * button_height) // 2

# Define the button colors
button_color_normal = (255, 255, 255)
button_color_hover = (200, 200, 200)
button_color_click = (150, 150, 150)

# Create the buttons
buttons = [
    {
        'text': 'Rock',
        'rect': pygame.Rect(button_x, button_y, button_width, button_height),
        'color': button_color_normal
    },
    {
        'text': 'Paper',
        'rect': pygame.Rect(button_x, button_y + button_height, button_width, button_height),
        'color': button_color_normal
    },
    {
        'text': 'Scissors',
        'rect': pygame.Rect(button_x, button_y + 2 * button_height, button_width, button_height),
        'color': button_color_normal
    }
]

# Set the initial game state
state = 'start'

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse position and button state
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_button = pygame.mouse.get_pressed()[0]

    # Update the game state
    if state == 'start':
        # Check if the mouse button was pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Update the button colors based on the mouse position
            for button in buttons:
                if button['rect'].collidepoint(mouse_x, mouse_y):
                    button['color'] = button_color_click
        # Check if the mouse button was released
        if event.type == pygame.MOUSEBUTTONUP:
            # Reset the button colors
            for button in buttons:
                button['color'] = button_color_normal
            # Check if a button was clicked
            for button in buttons:
                if button['color'] == button_color_click:
                    state = 'countdown'
                    player_choice = button['text']
                    countdown = 3
                    countdown_start = pygame.time.get_ticks()

                if state == 'countdown':

                    # Decrement the countdown timer
                    elapsed_time = (pygame.time.get_ticks() - countdown_start) / 1000
                    if elapsed_time >= 1:
                        countdown -= 1
                        countdown_start = pygame.time.get_ticks()
                    # Draw the countdown on the screen
                    if countdown > 0:
                        text = f'{countdown}...'
                    else:
                        text = ''
                    text_surface = font.render(text, True, (0, 0, 0))
                    text_rect = text_surface.get_rect()
                    text_rect.center = (screen_width // 2, screen_height // 2)
                    screen.blit(text_surface, text_rect)



                    # Check if a button was clicked
                    for button in buttons:
                        if button['color'] == button_color_click:
                                state = 'countdown'
                                player_choice = button['text']
                                countdown = 3
                                countdown_start = pygame.time.get_ticks()
                                break

                            # Check if the countdown has reached 0
                        if countdown == 0:
                                state = 'result'
                                computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
                        if player_choice == computer_choice:
                                    result = 'Tie'
                        elif (player_choice == 'Rock' and computer_choice == 'Scissors') or (
                                        player_choice == 'Paper' and computer_choice == 'Rock') or (
                                        player_choice == 'Scissors' and computer_choice == 'Paper'):
                                    result = 'You win!'
                        else:
                                    result = 'You lose.'


            if state == 'result':
                # Draw the result on the screen
                        text = f'{result}'
                        text_surface = font.render(text, True, (0, 0, 0))
                        text_rect = text_surface.get_rect()
                        text_rect.center = (screen_width // 2, screen_height // 2)
                        screen.blit(text_surface, text_rect)

            # Update the screen
            pygame.display.update()
