import pygame

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Key Press Display")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 74)

def render_text(text, position):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, position)

def main():
    running = True
    keys_pressed = ""

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys_pressed = f"Key Pressed: {pygame.key.name(event.key)}"
            elif event.type == pygame.KEYUP:
                keys_pressed = ""

        render_text(keys_pressed, (50, HEIGHT // 2 - 50))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
