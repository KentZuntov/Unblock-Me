import pygame
import time

pygame.init()
võit_sound = pygame.mixer.Sound("unblockme.voit.wav")
pygame.mixer.music.load("Inspiring - and.mp3")

display_width = 640
display_height = 700

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Unblock Me")
clock = pygame.time.Clock()

x_change = 0
y_change = 0
#tulevikus meetod leveli sisselugemiseks
#loome blokid
main_block = pygame.rect.Rect(220, 220, 195, 95)
second_block = pygame.rect.Rect(520, 20, 95, 295)
third_block = pygame.rect.Rect(420, 320, 195, 95)
fourth_block = pygame.rect.Rect(20,20, 195, 95)
fifth_block = pygame.rect.Rect(220,320, 195, 95)
sixth_block = pygame.rect.Rect(220,20, 95, 195)
seventh_block = pygame.rect.Rect(320,20, 195, 95)
eighth_block = pygame.rect.Rect(420,120, 95, 195)
ninth_block = pygame.rect.Rect(20,220, 95, 195)
tenth_block = pygame.rect.Rect(20,420, 95, 195)
eleventh_block = pygame.rect.Rect(120, 420, 95, 195)
twelfth_block = pygame.rect.Rect(320, 420, 95, 195)
kolmteist = pygame.rect.Rect(420, 420, 195, 95)
neliteist = pygame.rect.Rect(420, 520, 195, 95)

blokid = [main_block, second_block, third_block, fourth_block, fifth_block, sixth_block, seventh_block, eighth_block, ninth_block, tenth_block, eleventh_block, twelfth_block, kolmteist, neliteist]

head_koordinaadid = [20, 120, 220, 320, 420, 520, 620]

def snap(x):
    for koordinaat in head_koordinaadid:
        if abs(koordinaat-x) <=40:
            return koordinaat
    return x

def pilt(x, y, pilt):
    image = pygame.image.load(pilt)
    gameDisplay.blit(image, (x,y))

def game_loop():
    pygame.mixer.music.play(-1)
    gameExit = False
    gamePlay = True
    current_block = None

    while not gameExit:
        prev_x = 0
        prev_y = 0
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for block in blokid:
                        if block.collidepoint(event.pos):
                            mouse_x, mouse_y = event.pos
                            x_change = block.x - mouse_x
                            y_change = block.y - mouse_y
                            current_block = block
                            break


            elif event.type == pygame.MOUSEBUTTONUP:
                if not current_block == None:
                    current_block.x = snap(current_block.x)
                    current_block.y = snap(current_block.y)
                    current_block = None

            elif event.type == pygame.MOUSEMOTION and gamePlay:
                if not current_block == None:
                    mouse_x, mouse_y = event.pos
                    prev_x = current_block.x
                    prev_y = current_block.y
                    if current_block == main_block:
                        if 20 < mouse_x + x_change < display_width:
                            current_block.x = mouse_x + x_change
                            for blokk in blokid:
                                if not blokk == current_block:
                                    if current_block.colliderect(blokk):
                                        current_block.x = prev_x
                                        break
                        if current_block.x > display_width - 200:
                            current_block.x = mouse_x + x_change
                            pygame.mixer.music.stop()
                            pygame.mixer.Sound.play(võit_sound)
                            gamePlay = False
                            
                    elif current_block.width > current_block.height:
                        if 20 < mouse_x + x_change < display_width - 20 - current_block.width:
                            current_block.x = mouse_x + x_change
                            for blokk in blokid:
                                if not blokk == current_block:
                                    if current_block.colliderect(blokk):
                                        current_block.x = prev_x
                                        break
                            
                    elif current_block.height > current_block.width:
                        if 20 < mouse_y + y_change < display_height - 80 - current_block.height:
                            current_block.y = mouse_y + y_change
                            for blokk in blokid:
                                if not blokk == current_block:
                                    if current_block.colliderect(blokk):
                                        current_block.y = prev_y
                                        break
                            
    
        pilt(0,0, "unblockme_taust.png")
        
        pilt(main_block.x, main_block.y, "200100blokk_main.png")
        pilt(second_block.x, second_block.y, "100300blokk_tav.png")
        pilt(third_block.x, third_block.y, "200100blokk_tav.png")
        pilt(fourth_block.x, fourth_block.y, "200100blokk_tav.png")
        pilt(fifth_block.x, fifth_block.y, "200100blokk_tav.png")
        pilt(sixth_block.x, sixth_block.y, "100200blokk_tav.png")
        pilt(seventh_block.x, seventh_block.y, "200100blokk_tav.png")
        pilt(eighth_block.x, eighth_block.y, "100200blokk_tav.png")
        pilt(ninth_block.x, ninth_block.y, "100200blokk_tav.png")
        pilt(tenth_block.x, tenth_block.y, "100200blokk_tav.png")
        pilt(eleventh_block.x, eleventh_block.y, "100200blokk_tav.png")
        pilt(twelfth_block.x, twelfth_block.y, "100200blokk_tav.png")
        pilt(kolmteist.x, kolmteist.y, "200100blokk_tav.png")
        pilt(neliteist.x, neliteist.y, "200100blokk_tav.png")
        
        if not gamePlay:
            pilt(0, 0, "voit.png")
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()