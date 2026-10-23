import pygame
import random
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")
font = pygame.font.SysFont("Arial", 50, bold=True)
clock = pygame.time.Clock()
pet_x = WIDTH // 2
pet_y = HEIGHT // 2
pet_speed = 5
pet_size = 50
food_list = []
for i in range(10):
    food_x = random.randint(0, WIDTH - 30)
    food_y = random.randint(0, HEIGHT - 30)
    food_list.append([food_x, food_y]) # Stores x and y together
food_size = 30
try:
    bg_img = pygame.transform.scale(pygame.image.load("background.png"), (WIDTH, HEIGHT))
    pet_img = pygame.transform.scale(pygame.image.load("pet.png"), (pet_size, pet_size))
    food_img = pygame.transform.scale(pygame.image.load("food.png"), (food_size, food_size))
    has_images = True
except:
    print("Images not found. Using simple colored shapes instead!")
    has_images = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pet_x > 0:
        pet_x -= pet_speed
    if keys[pygame.K_RIGHT] and pet_x < WIDTH - pet_size:
        pet_x += pet_speed
    if keys[pygame.K_UP] and pet_y > 0:
        pet_y -= pet_speed
    if keys[pygame.K_DOWN] and pet_y < HEIGHT - pet_size:
        pet_y += pet_speed
    pet_rect = pygame.Rect(pet_x, pet_y, pet_size, pet_size)
    for food in food_list[:]: 
        food_rect = pygame.Rect(food[0], food[1], food_size, food_size)
        if pet_rect.colliderect(food_rect):
            food_list.remove(food)
    if has_images:
        screen.blit(bg_img, (0, 0)) 
        for food in food_list:
            screen.blit(food_img, (food[0], food[1]))
        screen.blit(pet_img, (pet_x, pet_y))
    else:
        screen.fill((200, 230, 200))
        for food in food_list:
            pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], food_size, food_size)) 
        pygame.draw.rect(screen, (0, 0, 255), (pet_x, pet_y, pet_size, pet_size)) 
    if len(food_list) == 0:
        text_surface = font.render("Game Completed!", True, (0, 100, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()