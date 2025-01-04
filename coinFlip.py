from random import choice as randchoice
import pygame

pygame.font.init()
pygame.init()

# Defining values and variables
heads, tails = 0, 0
bg_color = (151, 215, 255)
width = height = 800
win = pygame.display.set_mode((width, height))
coin_rect = pygame.Rect(275, 275, 250, 250)
coin_rect_side = pygame.Rect(0, 0, 250, 25)

heads_img = pygame.transform.scale(pygame.image.load("headsSide.png"), (250, 250))
tails_img = pygame.transform.scale(pygame.image.load("tailsSide.png"), (250, 250))

# Defining texts
font = pygame.font.SysFont("ariel", 40)
flip_text = font.render("F = Flip", 1, "black")
heads_text = font.render(f"Heads: {heads}", 1, "black")
tails_text = font.render(f"Tails: {tails}", 1, "black")

# Significant variables
can_flip = True
choices = ["heads", "tails"]
result = ""

def flipped(flippable):
    global result, heads
    if not flippable:
        result = randchoice(choices)
        for i in range(0, 16):
            # Begins animation loop
            win.fill(bg_color)
            # Coin moves up
            if i <= 7:
                # Flips coin to show face or side view
                if i % 2 == 0:
                    coin_rect_side.center = coin_rect.center
                    coin_rect_side.y = coin_rect_side.y - 25
                    pygame.draw.rect(win, "black", coin_rect_side)
                else:
                    coin_rect.center = coin_rect_side.center
                    coin_rect.y = coin_rect.y - 25
                    pygame.draw.rect(win, bg_color, coin_rect)
                    win.blit(randchoice([heads_img, tails_img]), coin_rect)
            # Coin moves down
            else:
                # Also flips coin
                if i % 2 == 0:
                    coin_rect_side.center = coin_rect.center
                    coin_rect_side.y = coin_rect_side.y + 25
                    pygame.draw.rect(win, "black", coin_rect_side)
                else:
                    coin_rect.center = coin_rect_side.center
                    coin_rect.y = coin_rect.y + 25
                    pygame.draw.rect(win, bg_color, coin_rect)
                    win.blit(randchoice([heads_img, tails_img]), coin_rect)
            pygame.time.delay(50)
            pygame.display.flip()


def stats():
    # If the re-render isn't done, the counter stays at 0
    global heads_text, tails_text
    heads_text = font.render(f"Heads: {heads}", 1, "black")
    tails_text = font.render(f"Tails: {tails}", 1, "black")


def draw():
    # Renders elements onto screen
    global heads, tails
    win.fill(bg_color)
    stats()
    win.blit(flip_text, (400 - flip_text.get_width() / 2, 100 - flip_text.get_height() / 8))
    win.blit(heads_text, (300 - heads_text.get_width() / 2, 150 - heads_text.get_height() / 8))
    win.blit(tails_text, (500 - tails_text.get_width() / 2, 150 - tails_text.get_height() / 8))
    if result == "heads":
        win.blit(heads_img, coin_rect)
    else:
        win.blit(tails_img, coin_rect)
    pygame.display.flip()


run = True

# Runs the game
while run:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                can_flip = False
                flipped(can_flip)
                if result == "heads":
                    heads += 1
                else:
                    tails += 1
                can_flip = True

pygame.quit()
