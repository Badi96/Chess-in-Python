import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900 
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two player Pygame chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 20)
timer = pygame.time.Clock() # controls the speed of the game, pfs etc. 
fps = 60 
# game variables and images

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []

# 0 - whites turn, no selection: 1 - whites turn, pice selected: 2 - blacks turn, no selction: 3 - black turn, piece selected
turn_step = 0
selection = 100 # value of selected piece
valid_moves = []

#load in game oice images (queen, king, roook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
white_promotions = ['bishop', 'knight', 'rook', 'queen']
white_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
black_promotions = ['bishop', 'knight', 'rook', 'queen']
black_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# check variables/ flashing counter


#draw main board
def draw_board():
    for i in range(32):
        column = i % 4 #check for remainder when diving by 4
        row = i // 4 # Divide by 4 and round down to the fullest interger
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 -(column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 -(column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100 ])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100 ], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT ], 5)
        status_text = ['White: select a Piece to move!', 'White: select a Destination!', 
                        'Black: select a Piece to move!', 'Black: select a Destination!']

        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        
        #draw some lines
        #for i in range(9):
        #    pygame.draw.line(screen, 'black', (0, 100*i), (800, 100*i), 2)
        #    pygame.draw.line(screen, 'black', (100*i,0 ), ( 100*i, 800), 2)

# draw pices unto board
def draw_pices():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))

        #highlight pices
        if turn_step < 2:
            #white's turn
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0]*100 + 1,  white_locations[i][1]*100 + 1, 100, 100], 2)


    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else: 
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
             #highlight pices
        if turn_step >= 2:
            #black's turn
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0]*100 + 1,  black_locations[i][1]*100 + 1, 100, 100], 2)


#function to check all pieces valid options on the board
def check_options(pieces, locations, turn):
    print('check options')
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)

        all_moves_list.append(moves_list)
    return all_moves_list

#check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list



# check for valid moves for just selectd pice
def check_valid_moves():
    if turn_step < 2:
        print('white')
        options_list = white_options
    else:
        options_list = black_options
    print('selection: ' + str(selection))
    print('options_list' + str(options_list))
    valid_options = options_list[selection]
    return valid_options


# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True

while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pices()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    # Event handling (mouse, keyborard, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # check click event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100 # shows the x coordinate of click
            y_coord = event.pos[1] // 100 # shows the y coordinate of click
            click_coords = (x_coord, y_coord)
            
            if turn_step <= 1:
                #Black turn
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords) # grabs the index of the pice
                    if turn_step == 0:
                        turn_step = 1 # change to select turn step
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords) #index of the captured black pice
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100 # to make no piece selected
                    valid_moves = [] # for re-calculating the valid moves in new turn
            
            if turn_step > 1:
                #White turn
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords) # grabs the index of the pice
                    if turn_step == 2:
                        turn_step = 3 # change to select turn step
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords) #index of the captured black pice
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0 
                    selection = 100 # to make no piece selected
                    valid_moves = [] # for re-calculating the valid moves in new turn



    pygame.display.flip()
pygame.quit()