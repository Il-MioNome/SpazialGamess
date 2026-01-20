from pgzero_api_stub import *
import pgzrun
import random

WIDTH = 800
HEIGHT = 600
FPS = 60
TITLE = f"SpaceCombat (Set to {FPS} FPS)"

background = Actor("bg", (400,300))
game_over_background = Actor("game_over", (400,300))
player = Actor("spacecraft", (400,540), size=(10,10))
alien1 = Actor("nemico", (random.randint(30,770), random.randint(-60, -20)))
alien2 = Actor("nemico", (random.randint(30,770), random.randint(-100, -60)))
alien3 = Actor("nemico", (random.randint(30,770), random.randint(-140, -100)))
alien4 = Actor("nemico", (random.randint(30,770), random.randint(-180, -140)))
alien5 = Actor("nemico", (random.randint(30,770), random.randint(-220, -180)))
alien6 = Actor("nemico", (random.randint(30,770), random.randint(-260, -220)))

score = 0
bigger_score = 0
vite = 3
game_over = False
collisione = False
livello = 1
start = False

def draw():
    global game_over
    global vite
    global score
    global start
    
    background.draw()
    player.draw()
    alien1.draw()
    alien2.draw()
    alien3.draw()
    alien4.draw()
    alien5.draw()
    alien6.draw()
    if game_over == True:
        game_over_background.draw()
        screen.draw.text(f"Max score: {bigger_score}", (325, 190), color="green", fontsize=40)
    else:
        pass
    
    screen.draw.text(f"Life: {vite}", (10, 10), color="green", fontsize=40)
    screen.draw.text(f"Score: {score}", (10, 40), color="green", fontsize=40)
    screen.draw.text(f"Level: {livello}", (10, 70), color="green", fontsize=40)
    screen.draw.text(f"Max score: {bigger_score}", (10, 100), color="green", fontsize=40)
    
    if start == False:
        background.draw()
        screen.draw.text("Let's Start!", (275, 240), color="green", fontsize=72)
        screen.draw.text("Press 'ENTER' for start!", (260, 320), color="green", fontsize=40)
        screen.draw.text("Press 'R' for re-start!", (320, 365), color="green", fontsize=25)
        
def update(dt):
    global score
    global vite
    global bigger_score
    global game_over
    global collisione
    global livello
    
    if (keyboard.left or keyboard.a) and player.x > 30:
        if livello == 1:
            player.x = player.x - 5
        elif livello == 2:
            player.x = player.x - 6
        elif livello == 3:
            player.x = player.x - 8
        elif livello == 4:
            player.x = player.x - 10
        elif livello == 5:
            player.x = player.x - 12
            
    elif (keyboard.right or keyboard.d) and player.x < 770:
        if livello == 1:
            player.x = player.x + 5
        elif livello == 2:
            player.x = player.x + 6
        elif livello == 3:
            player.x = player.x + 8
        elif livello == 4:
            player.x = player.x + 10
        elif livello == 5:
            player.x = player.x + 12
        
    elif (keyboard.up or keyboard.w) and player.y > 250:
        if livello == 1:
            player.y = player.y - 5
        elif livello == 2:
            player.y = player.y - 6
        elif livello == 3:
            player.y = player.y - 8
        elif livello == 4:
            player.y = player.y - 10
        elif livello == 5:
            player.y = player.y - 12
    
    elif (keyboard.down or keyboard.s) and player.y < 570:
        if livello == 1:
            player.y = player.y + 5
        elif livello == 2:
            player.y = player.y + 6
        elif livello == 3:
            player.y = player.y + 8
        elif livello == 4:
            player.y = player.y + 10
        elif livello == 5:
            player.y = player.y + 12
        
    if (player.colliderect(alien1.inflate(-40, -40)) or player.colliderect(alien2.inflate(-40, -40)) or player.colliderect(alien3.inflate(-40, -40)) or player.colliderect(alien4.inflate(-40, -40)) or player.colliderect(alien5.inflate(-40, -40)) or player.colliderect(alien6.inflate(-40, -40))) and not collisione:
        vite -= 1
        collisione = True
    
    if not (player.colliderect(alien1.inflate(-40, -40)) or player.colliderect(alien2.inflate(-40, -40)) or player.colliderect(alien3.inflate(-40, -40)) or player.colliderect(alien4.inflate(-40, -40)) or player.colliderect(alien5.inflate(-40, -40)) or player.colliderect(alien6.inflate(-40, -40))) and collisione:
        collisione = False
    
    if game_over == False:
        
        #alieno1
        if alien1.y >= 610:
            alien1.x = random.randint(30, 770)
            alien1.y = random.randint(-700, -670)
        else:
            if score < 5:
                alien1.y = alien1.y + 2
            elif score > 4 and score < 10:
                alien1.y = alien1.y + 5
            elif score > 9 and score < 15:
                alien1.y = alien1.y + 8
            elif score > 14 and score < 20:
                alien1.y = alien1.y + 11
            elif score > 19:
                alien1.y = alien1.y + 14
            
        #alieno2
        if alien2.y >= 610:
            alien2.x = random.randint(30, 770)
            alien2.y = random.randint(-700, -670)
        else:
            if score < 5:
                alien2.y = alien2.y + 2
            elif score > 4 and score < 10:
                alien2.y = alien2.y + 5
            elif score > 9 and score < 15:
                alien2.y = alien2.y + 8
            elif score > 14 and score < 20:
                alien2.y = alien2.y + 11
            elif score > 19:
                alien2.y = alien2.y + 14
            
        #alieno3
        if alien3.y >= 610:
            alien3.x = random.randint(30, 770)
            alien3.y = random.randint(-700, -670)
        else:
            if score < 5:
                alien3.y = alien3.y + 2
            elif score > 4 and score < 10:
                alien3.y = alien3.y + 5
            elif score > 9 and score < 15:
                alien3.y = alien3.y + 8
            elif score > 14 and score < 20:
                alien3.y = alien3.y + 11
            elif score > 19:
                alien3.y = alien3.y + 14
            
        #alieno4
        if alien4.y >= 610:
            alien4.x = random.randint(30, 770)
            alien4.y = random.randint(-700, -670)
        else:
            if score < 5:
                alien4.y = alien4.y + 2
            elif score > 4 and score < 10:
                alien4.y = alien4.y + 5
            elif score > 9 and score < 15:
                alien4.y = alien4.y + 8
            elif score > 14 and score < 20:
                alien4.y = alien4.y + 11
            elif score > 19:
                alien4.y = alien4.y + 14
            
        #alieno5
        if alien5.y >= 610:
            alien5.x = random.randint(30, 770)
            alien5.y = random.randint(-700, -670)
        else:
            if score < 5:
                alien5.y = alien5.y + 2
            elif score > 4 and score < 10:
                alien5.y = alien5.y + 5
            elif score > 9 and score < 15:
                alien5.y = alien5.y + 8
            elif score > 14 and score < 20:
                alien5.y = alien5.y + 11
            elif score > 19:
                alien5.y = alien5.y + 14
            
        #alieno6
        if alien6.y >= 610:
            score += 1
            alien6.x = random.randint(30, 770)
            alien6.y = random.randint(-700, -670)
        else:
            if score < 5:
                alien6.y = alien6.y + 2
            elif score > 4 and score < 10:
                livello = 2
                alien6.y = alien6.y + 5
            elif score > 9 and score < 15:
                livello = 3
                alien6.y = alien6.y + 8
            elif score > 14 and score < 20:
                livello = 4
                alien6.y = alien6.y + 11
            elif score > 19:
                livello = 5
                alien6.y = alien6.y + 14
        
    else:
        alien1.y = random.randint(-60, -20)
        alien2.y = random.randint(-100, -60)
        alien3.y = random.randint(-140, -100)
        alien4.y = random.randint(-180, -140)
        alien5.y = random.randint(-220, -180)
        alien6.y = random.randint(-260, -220)
        if score > bigger_score:
            bigger_score = score
 
    if vite == 0:
        game_over = True
    
def on_key_down(key):
    global vite
    global game_over
    global score
    global livello
    global start
    
    if keyboard.RETURN and game_over == True:
        vite = 3
        score = 0
        livello = 1
        game_over = False
        
    if keyboard.RETURN and start == False:
        vite = 3
        score = 0
        livello = 1
        game_over = False
        start = True
        #--------------------------------------
        alien1.y = random.randint(-60, -20)
        alien2.y = random.randint(-100, -60)
        alien3.y = random.randint(-140, -100)
        alien4.y = random.randint(-180, -140)
        alien5.y = random.randint(-220, -180)
        alien6.y = random.randint(-260, -220)
        #----------------------------------------
    
    if keyboard.r and start == True and game_over == False:
        vite = 3
        score = 0
        livello = 1
        game_over = False
        start = True
        #--------------------------------------
        alien1.x = random.randint(30, 770)
        alien2.x = random.randint(30, 770)
        alien3.x = random.randint(30, 770)
        alien4.x = random.randint(30, 770)
        alien5.x = random.randint(30, 770)
        alien6.x = random.randint(30, 770)
        #--------------------------------------
        alien1.y = random.randint(-60, -20)
        alien2.y = random.randint(-100, -60)
        alien3.y = random.randint(-140, -100)
        alien4.y = random.randint(-180, -140)
        alien5.y = random.randint(-220, -180)
        alien6.y = random.randint(-260, -220)
        #----------------------------------------
    
pgzrun.go()