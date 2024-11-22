# run.py
import pygame
import sys
from agent import Agent
from environment import Environment

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
GRID_SIZE = 40
STATUS_WIDTH = 300
BACKGROUND_COLOR = (255, 255, 255)
BARRIER_COLOR = (0, 0, 0)       # Barrier color is black
TASK_COLOR = (255, 0, 0)        # Task color is red
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (0, 200, 0)
BUTTON_HOVER_COLOR = (0, 255, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
MOVEMENT_DELAY = 200  # Milliseconds between movements

def main():
    pygame.init()

    # Set up display with an additional status panel
    screen = pygame.display.set_mode((WINDOW_WIDTH + STATUS_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pygame AI Grid Simulation")

    # Clock to control frame rate
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    # Initialize environment and agent
    environment = Environment(WINDOW_WIDTH, WINDOW_HEIGHT, GRID_SIZE, num_tasks=5, num_barriers=15)
    algorithm = "UCS"  # Start with UCS by default
    agent = Agent(environment, GRID_SIZE, algorithm=algorithm)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(agent)

    # Start button positioned on the right side (status panel)
    button_width, button_height = 100, 50
    button_x = WINDOW_WIDTH + (STATUS_WIDTH - button_width) // 2
    button_y = WINDOW_HEIGHT // 2 - button_height // 2
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    simulation_started = False

    # Toggle button for algorithm
    toggle_button_rect = pygame.Rect(button_x, button_y + 60, button_width, button_height)

    # Variables for movement delay
    last_move_time = pygame.time.get_ticks()

    # Main loop
    running = True
    while running:
        clock.tick(60)  # Limit to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not simulation_started and button_rect.collidepoint(event.pos):
                    # Start the simulation
                    simulation_started = True
                    agent.total_path_cost = 0
                    if environment.task_locations:
                        agent.find_nearest_task()
                elif toggle_button_rect.collidepoint(event.pos):
                    # Toggle algorithm between UCS and A*
                    algorithm = "A*" if algorithm == "UCS" else "UCS"
                    agent.algorithm = algorithm
                    agent.total_path_cost = 0
                    simulation_started = False  # Reset simulation on toggle
                    agent.position = [0, 0]  # Reset agent's position
                    agent.rect.topleft = (0, 0)
                    agent.task_completed = 0
                    agent.completed_tasks = []
                    environment.task_locations = environment.generate_tasks(5)  # Reset tasks

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw grid and barriers
        for x in range(environment.columns):
            for y in range(environment.rows):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # Draw grid lines

        # Draw barriers
        for (bx, by) in environment.barrier_locations:
            barrier_rect = pygame.Rect(bx * GRID_SIZE, by * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BARRIER_COLOR, barrier_rect)

        # Draw tasks with numbers
        for (tx, ty), task_number in environment.task_locations.items():
            task_rect = pygame.Rect(tx * GRID_SIZE, ty * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, TASK_COLOR, task_rect)
            # Draw task number
            task_num_surface = font.render(str(task_number), True, (255, 255, 255))
            task_num_rect = task_num_surface.get_rect(center=task_rect.center)
            screen.blit(task_num_surface, task_num_rect)

        # Draw agent
        all_sprites.draw(screen)

        # Display status panel
        status_x = WINDOW_WIDTH + 10
        algorithm_text = f"Algorithm: {algorithm}"
        task_status_text = f"Tasks Completed: {agent.task_completed}"
        position_text = f"Position: {agent.position}"
        completed_tasks_text = f"Completed Tasks: {agent.completed_tasks}"
        path_cost_text = f"Total Path Cost: {agent.total_path_cost}"

        algorithm_surface = font.render(algorithm_text, True, TEXT_COLOR)
        status_surface = font.render(task_status_text, True, TEXT_COLOR)
        position_surface = font.render(position_text, True, TEXT_COLOR)
        completed_tasks_surface = font.render(completed_tasks_text, True, TEXT_COLOR)
        path_cost_surface = font.render(path_cost_text, True, TEXT_COLOR)

        screen.blit(algorithm_surface, (status_x, 20))
        screen.blit(status_surface, (status_x, 50))
        screen.blit(position_surface, (status_x, 80))
        screen.blit(completed_tasks_surface, (status_x, 110))
        screen.blit(path_cost_surface, (status_x, 140))

        # Draw the start button if simulation hasn't started
        if not simulation_started:
            mouse_pos = pygame.mouse.get_pos()
            button_color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(screen, button_color, button_rect)
            button_text = font.render("Start", True, BUTTON_TEXT_COLOR)
            text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, text_rect)
        else:
            # Automatic movement with delay
            # Automatic movement with reduced delay
            if simulation_started:
                current_time = pygame.time.get_ticks()
                if current_time - last_move_time > 50:  # Reduced delay to 50ms for faster movement
                    if not agent.moving and environment.task_locations:
                        # Find the nearest task
                        agent.find_nearest_task()
                    elif agent.moving:
                        agent.move()
                    last_move_time = current_time


        # Draw the algorithm toggle button
        toggle_button_color = BUTTON_HOVER_COLOR if toggle_button_rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
        pygame.draw.rect(screen, toggle_button_color, toggle_button_rect)
        toggle_text = font.render("Toggle", True, BUTTON_TEXT_COLOR)
        toggle_text_rect = toggle_text.get_rect(center=toggle_button_rect.center)
        screen.blit(toggle_text, toggle_text_rect)

        # Draw the status panel separator
        pygame.draw.line(screen, (0, 0, 0), (WINDOW_WIDTH, 0), (WINDOW_WIDTH, WINDOW_HEIGHT))

        # Update the display
        pygame.display.flip()

    # Quit Pygame properly
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
