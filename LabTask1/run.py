import pygame
from agent import Agent
from environment import Environment

def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Agent-Environment Simulation")

    
    env = Environment(width=600, height=400)  
    agent = Agent(environment=env)

    agent.size = (20, 20)

 
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            agent.move("up")
        if keys[pygame.K_DOWN]:
            agent.move("down")
        if keys[pygame.K_LEFT]:
            agent.move("left")
        if keys[pygame.K_RIGHT]:
            agent.move("right")

        
        screen.fill((255, 255, 255))

     
        position = agent.status()
        rect_position = (position[0], position[1], agent.size[0], agent.size[1])
        pygame.draw.rect(screen, (0, 0, 255), rect_position)

        position_text = font.render(f"Position: ({position[0]}, {position[1]})", True, (0, 0, 0))
        screen.blit(position_text, (10, 10))

        pygame.display.flip()

        pygame.time.Clock().tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
