import pygame
from random import *

pygame.init()

GREEN = (28, 201, 37)
Black = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

clock = pygame.time.Clock()
window = pygame.display.set_mode((500, 500))
window.fill(GREEN)

class TextArea():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    
    def set_text(self, text, fsize =12, text_color=Black):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text,True, text_color)

    def draw(self, shift_x=0, shift_y =0):
        pygame.draw.rect(window,self.fill_color,self.rect)
        window.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))

quest_card = TextArea(120,100,290,70, LIGHT_BLUE)
quest_card.set_text("Питання", 75)

ans_card = TextArea(120,240,290,70, LIGHT_BLUE)
ans_card.set_text("Відповідь", 75)

quest_card.draw(10,10)
ans_card.draw(10,10)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint (1,4)
                if num == 1:
                    quest_card.set_text('Що вивчаєш в логіці?', 25)
                if num == 2:
                    quest_card.set_text('Якою мовою говорять в Франції?', 25)
                if num == 3:
                    quest_card.set_text('що росте на вишні?', 25)
                if num == 4:
                    quest_card.set_text('що росте на яблуні?', 25)
                quest_card.draw(10, 25)

            if event.key == pygame.K_a:
                num = randint (1,4)
                if num ==1:
                    ans_card.set_text('Python', 35)
                if num ==2:
                    ans_card.set_text('Французькою', 35)
                if num ==3:
                    ans_card.set_text('Вишні', 35)
                if num ==4:
                    ans_card.set_text('Яблука', 35)

                ans_card.draw(10, 25)

    pygame.display.update()
    clock.tick(60) 
        
pygame.quit()