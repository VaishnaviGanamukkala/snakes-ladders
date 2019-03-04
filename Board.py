import pygame, sys, random

pygame.init()

display_width = 1250
display_height = 700
CAPTION = "Snakes and Ladders"

game_wn = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(CAPTION)

frame_rate = pygame.time.Clock()
BG = pygame.image.load('images/BrownBG.jpg')

board_width = 600
board_ht = 600
block_wd = board_width / 10
block_ht = board_ht / 10
gap = 2
maxNo = 100
coin_rad = 20

x_start = (display_width - board_width) / 2
y_start = (display_height - board_ht) / 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
VIOLET = (138, 43, 226)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
SAND = (238, 232, 170)
FONT = 'HarryP'
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99}
SNAKES = {17: 7, 54: 34, 62: 19, 64: 60, 87: 36, 93: 73, 95: 75, 98:79}
position = {}

def SndL_board():
    colors = [ORANGE, SAND]
    ladder_img = pygame.image.load('images/lad.gif')
    ladder_img = pygame.transform.scale(ladder_img, (40, 40))
    snake_img = pygame.image.load('images/snake.png')
    snake_img = pygame.transform.scale(snake_img, (40, 40))

    for y in range(10):
        turn(colors)
        i = maxNo - (10 * y)
        for x in range(10):
            turn(colors)

            x_cordinate = x*(block_wd + gap) + x_start
            y_cordinate = y*(block_ht + gap) + y_start
            block = pygame.Rect(x_cordinate, y_cordinate, block_wd, block_ht)
            pygame.draw.rect(game_wn, colors[0], block)

            if y % 2 == 0:
                j = i - x

            else:
                j = i + x - 9
            position[j] = (int(x_cordinate + (block_wd / 2)), int(y_cordinate + (block_ht / 2)))

            if j in LADDERS.keys():
                game_wn.blit(ladder_img, (position[j][0] - 10, position[j][1] - 10))
            elif j in SNAKES.keys():
                game_wn.blit(snake_img, (position[j][0] - 10, position[j][1] - 10))
            
            text_display(20, str(j), BLACK, (x_cordinate + gap, y_cordinate + gap))

def text_display(font_size, message, text_colour, cordinates):
    font = pygame.font.SysFont(FONT, font_size)
    text = font.render(message, True, text_colour)
    game_wn.blit(text, cordinates)

def button(box, rectX_st, rectY_st, wd, ht, font_size, message, text_colour, cordinates):
    mouse = pygame.mouse.get_pos()

    if rectX_st + wd > mouse[0] > rectX_st and rectY_st + ht > mouse[1] > rectY_st:
        key = pygame.draw.rect(game_wn, VIOLET, box)

    else:
        key = pygame.draw.rect(game_wn, INDIGO, box)

    text_display(font_size, message, text_colour, cordinates)
    pygame.display.update()

def roll_dice():
    dice = pygame.image.load('images/dice.gif')
    dice = pygame.transform.scale(dice, (250, 250))
    game_wn.blit(dice, (960, 90))

    dice_menu = pygame.Rect(996, 300, 200, 60)
    button(dice_menu, 996, 300, 200, 60, 50, "Roll Dice!", WHITE, (1030, 308))
    
    pygame.display.update()
    return dice_menu

def dice_img(n):
    one = pygame.image.load('images/1.png')
    one = pygame.transform.scale(one, (160, 160))
    two = pygame.image.load('images/2.png')
    two = pygame.transform.scale(two, (160, 160))
    three = pygame.image.load('images/3.png')
    three = pygame.transform.scale(three, (160, 160))
    four = pygame.image.load('images/4.png')
    four = pygame.transform.scale(four, (160, 160))
    five = pygame.image.load('images/5.png')
    five = pygame.transform.scale(five, (160, 160))
    six = pygame.image.load('images/6.png')
    six = pygame.transform.scale(six, (160, 160))

    dice = [one, two, three, four, five, six]
    game_wn.blit(dice[n-1], (1020, 100))

def dice_Rolled():
    return random.randint(1, 6)

def turn(players):
    players.append(players.pop(0))
    return players

def moves(start_pos, num_rolled):
    return min(start_pos + num_rolled, 100)

def encounter(pos):
    if pos in LADDERS.keys():
        pygame.draw.line(game_wn, GREEN, position[pos], position[LADDERS[pos]], 5)
        pygame.display.flip()
        pygame.time.delay(1000)
        return LADDERS[pos]
    elif pos in SNAKES.keys():
        pygame.draw.line(game_wn, RED, position[pos], position[SNAKES[pos]], 5)
        pygame.display.flip()
        pygame.time.delay(1000)
        return SNAKES[pos]
    else:
        return pos

def develop_list(record, n):
    if n == 1:
        return record[:2]
    else:
        return record[:n]

def win_img(winner):
    if winner == "Turn: Red" or winner == "Turn: Computer":
        logo = pygame.image.load('images/Red.png')
        game_wn.blit(logo, (500, 100))
    elif winner == "Turn: Yellow" or winner == "Turn: You":
        logo = pygame.image.load('images/Yellow.png')
        game_wn.blit(logo, (500, 100))
    elif winner == "Turn: Blue":
        logo = pygame.image.load('images/Blue.png')
        game_wn.blit(logo, (500, 100))
    elif winner == "Turn: Green":
        logo = pygame.image.load('images/Green.png')
        game_wn.blit(logo, (500, 100))

red_pos = (162, 127)
yellow_pos = (162, 281)
blue_pos = (162, 435)
green_pos = (162, 589)

def Coin(colour, pos):
    return pygame.draw.circle(game_wn, colour, pos, coin_rad)

game = False
colour = ["Turn: Red", "Turn: Yellow", "Turn: Blue", "Turn: Green"]
players = [red_pos, yellow_pos, blue_pos, green_pos]
pos = [0, 0, 0, 0]
game_piece = [RED, YELLOW, BLUE, GREEN]


game_wn.blit(BG, (0, 0))

def play1():
    player = pygame.Rect(300, 300, 200, 60)
    button(player, 300, 300, 200, 60, 50, "1 Player", WHITE, (340, 305))
    
    return player

def play2():
    player = pygame.Rect(750, 300, 200, 60)
    button(player, 750, 300, 200, 60, 50, "2 Players", WHITE, (780, 305))
    
    return player

def play3():
    player = pygame.Rect(300, 600, 200, 60)
    button(player, 300, 600, 200, 60, 50, "3 Players", WHITE, (340, 605))
    
    return player

def play4():
    player = pygame.Rect(750, 600, 200, 60)
    button(player, 750, 600, 200, 60, 50, "4 Players", WHITE, (780, 605))
    
    return player

def player_num():
    text_display(100, "Select Players", WHITE, (480, 0))

    p1 = pygame.image.load('images/p1.png')
    p1 = pygame.transform.scale(p1, (200, 200))
    game_wn.blit(p1, (300, 100))
    p2 = pygame.image.load('images/p2.png')
    p2 = pygame.transform.scale(p2, (200, 200))
    game_wn.blit(p2, (750, 100))
    p3 = pygame.image.load('images/p3.png')
    p3 = pygame.transform.scale(p3, (200, 200))
    game_wn.blit(p3, (300, 400))
    p4 = pygame.image.load('images/p4.png')
    p4 = pygame.transform.scale(p4, (200, 200))
    game_wn.blit(p4, (750, 400))

player_num()
pygame.display.update()
select_player = False
while not select_player:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            select_player = True
            pygame.quit()
            sys.exit()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if play1().collidepoint(mouse) and click[0]:
        n = 1
        select_player = True
    elif play2().collidepoint(mouse) and click[0]:
        n = 2
        select_player = True
    elif play3().collidepoint(mouse) and click[0]:
        n = 3
        select_player = True
    elif play4().collidepoint(mouse) and click[0]:
        n = 4
        select_player = True

players = develop_list(players, n)
pos = develop_list(pos, n)
game_piece = develop_list(game_piece, n)
if n == 1:
    colour = ["Turn: Computer", "Turn: You"]
else:
    colour = colour[:n]

if n == 1:
    n = 2

win = pygame.mixer.Sound('images/win.wav')
dice_roll = pygame.mixer.Sound('images/dice.wav')

while not game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = True
            pygame.quit()
            sys.exit()

    game_wn.blit(BG, (0, 0))
    SndL_board()
    text_display(50, colour[0], WHITE, (70, 50))
    for i in range(0, n):
        Coin(game_piece[i], players[i])
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (roll_dice().collidepoint(mouse) and click[0]) or (colour[0] == "Turn: Computer"):
        pygame.mixer.Sound.play(dice_roll)
        dice = dice_Rolled()
        pos[0] = moves(pos[0], dice)
        players[0] = position[pos[0]]

        game_wn.blit(BG, (0, 0))
        SndL_board()
        dice_img(dice)
        text_display(50, colour[0], WHITE, (70, 50))

        for i in range(0, n):
            Coin(game_piece[i], players[i])

        pygame.display.flip()
        pygame.time.delay(2000)

        if pos[0] == 100:
            pygame.time.delay(1000)
            pygame.mixer.Sound.play(win)
            game_wn.blit(BG, (0, 0))
            win_img(colour[0])
            msg = colour[0].split(" ")[1] + " Won!"
            text_display(120, msg, WHITE, (400, 400))
            pygame.display.update()
            pygame.time.delay(5000)
            game = True
            break

        if encounter(pos[0]) != pos[0]:
            pos[0] = encounter(pos[0])
            players[0] = position[pos[0]]

            game_wn.blit(BG, (0, 0))
            SndL_board()
            dice_img(dice)
            text_display(50, colour[0], WHITE, (70, 50))
            for i in range(0, n):
                Coin(game_piece[i], players[i])

            pygame.display.flip()
            pygame.time.delay(1000)

        pygame.time.delay(1000)

        if dice != 6:
            turn(players)
            turn(colour)
            turn(pos)
            turn(game_piece)
