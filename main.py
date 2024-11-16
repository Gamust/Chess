import pygame
from sys import exit
import functions
import time
import check
import configuration

pygame.init()

# SIZE
WIDTH = 1200
HEIGHT = 800
PADDING = 20

BOARD_WIDTH = ((2/3)*WIDTH) - (PADDING*2)
BOARD_HEIGHT = HEIGHT  - (PADDING*2)

TILE = (BOARD_WIDTH/8, BOARD_HEIGHT/8)
SIZE = BOARD_WIDTH/8

IMAGE_SIZE = TILE

WIDTH_PROMOTION = ((WIDTH-BOARD_WIDTH)/2 - SIZE)/2
PROMOTION_PADDING = 30


# COLORS
BROWN = (100, 50, 0)
LIGHT_BROWN = (255, 200, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE = (175,238,238)
GOLD = (218,165,32)


# Setup the screen and FPS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Python")
Clock = pygame.time.Clock()


# Get the board in the middle of the screen
board = pygame.Surface((BOARD_WIDTH,BOARD_HEIGHT))
board_rect = board.get_rect(center = (WIDTH/2,HEIGHT/2))


# Creates the tiles used in the board
white_tile = pygame.Surface(TILE)
white_tile.fill(BROWN) # black tiles
black_tile = pygame.Surface(TILE)
black_tile.fill(LIGHT_BROWN) # white tiles

# Creates the highlight tile for the possible moves
highlight = pygame.Surface(TILE)
highlight.fill(TURQUOISE)

# Creates the promotion tile
promotion_tile = pygame.Surface(TILE)
promotion_tile.fill(GOLD)

# Creates the cleaning tile to remove the promotion tiles
cleaning = pygame.Surface(((WIDTH-BOARD_WIDTH)/2,HEIGHT))
cleaning.fill(BLACK)


# INSERT CHESS PIECES
def load_and_scale_image(filename):
    image = pygame.image.load(configuration.get_image_path(filename)).convert_alpha()
    return pygame.transform.scale(image, IMAGE_SIZE)

bpawn = load_and_scale_image("BPawn.png")
wpawn = load_and_scale_image("WPawn.png")
brook = load_and_scale_image("BRook.png")
wrook = load_and_scale_image("WRook.png")
bking = load_and_scale_image("BKing.png")
wking = load_and_scale_image("WKing.png")
bqueen = load_and_scale_image("BQueen.png")
wqueen = load_and_scale_image("WQueen.png")
bknight = load_and_scale_image("BKnight.png")
wknight = load_and_scale_image("WKnight.png")
bbishop = load_and_scale_image("BBishop.png")
wbishop = load_and_scale_image("WBishop.png")


# Game creation
STARTING_GAME = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w QKqk - 0 0"
test_game = "8/8/8/8/q7/8/8/8 w QKqk - 0 0"
positionOfAllPieces,turn,_,_,_,_ = functions.Fen(STARTING_GAME)


movesHighlightFlag = False
flag_promotion = False
move_check = True
first_click_piece = 0
second_click_piece = 0
temp_piece = ""
promotion_list_of_tiles = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    # Creation of the board
    Cells = []
    for row in range(8):
        for col in range(8):
            x = board_rect.topleft[0] + col * SIZE
            y = board_rect.topleft[1] + row * SIZE
            rect = pygame.Rect(x, y, SIZE, SIZE)
            Cells.append(rect)
            if (row + col) % 2 == 0:
                tile = white_tile
            else:
                tile = black_tile
            screen.blit(tile, (x, y))
    
    # Check for checkmate and switchs turns
    result = check.checkmate(positionOfAllPieces,turn)

    # computer plays if game is ongoing on the black turn
    if result == 0:
        if not turn:
            functions.randcomputer(positionOfAllPieces, turn)
            turn = functions.change_turn(turn)
            time.sleep(0.5)
        

    # Mouse actions
    click, _, _ = pygame.mouse.get_pressed()
    if click:
        mouse = pygame.mouse.get_pos()
        if not flag_promotion:
            for index,zz in enumerate(Cells):
                if zz.collidepoint(mouse):
                    # position of click and turn on and off highlight
                    if not movesHighlightFlag:
                        if positionOfAllPieces[index] == "empty":
                            break
                    movesHighlightFlag = not movesHighlightFlag
                    # Save the cell where the first click happened
                    if movesHighlightFlag:
                        first_click_index = index
                    

                    #move the piece on the second click
                    if not movesHighlightFlag:
                        # if positionOfAllPieces[first_click_index] != "empty":
                            if positionOfAllPieces[first_click_index].team == turn:
                                possible_moves = [x[0] for x in positionOfAllPieces[first_click_index].move(first_click_index,positionOfAllPieces)]
                                if index in possible_moves:
                                    temp = positionOfAllPieces[first_click_index].move(first_click_index,positionOfAllPieces)
                                    place_to_move = temp[possible_moves.index(index)]
                                    positionOfAllPieces = functions.piece_movement(first_click_index,place_to_move,positionOfAllPieces)
                                    second_click_piece = index
                                    

                                    # CHECK FOR PROMOTION
                                    if positionOfAllPieces[second_click_piece] != "empty" and positionOfAllPieces[second_click_piece].name == "pawn":
                                        if positionOfAllPieces[second_click_piece].isPromotion(second_click_piece):
                                            pieces = [wknight, wbishop, wrook, wqueen] if positionOfAllPieces[second_click_piece].team else [bknight, bbishop, brook, bqueen]
                                            for loop, piece in enumerate(pieces):
                                                y = int(PADDING + SIZE * 2 - PROMOTION_PADDING / 2 + loop * (SIZE + PROMOTION_PADDING / 3))
                                                prom_rect = pygame.Rect(WIDTH_PROMOTION, y, SIZE, SIZE)
                                                promotion_list_of_tiles.append(prom_rect)
                                                screen.blit(promotion_tile, (WIDTH_PROMOTION, y))
                                                screen.blit(piece, (WIDTH_PROMOTION, y))
                                            flag_promotion = True
                                            continue
                                    turn = functions.change_turn(turn)
                    time.sleep(0.2)
    
        for index,zx in enumerate(promotion_list_of_tiles):
            if zx.collidepoint(mouse):
                if index == 0:
                    positionOfAllPieces = positionOfAllPieces[second_click_piece].Promotion(second_click_piece,positionOfAllPieces,0)
                    promotion_list_of_tiles = []
                    screen.blit(cleaning,(0,0))
                    flag_promotion = False
                    turn = functions.change_turn(turn)
                elif index == 1:
                    positionOfAllPieces = positionOfAllPieces[second_click_piece].Promotion(second_click_piece,positionOfAllPieces,1)
                    promotion_list_of_tiles = []
                    screen.blit(cleaning,(0,0))
                    flag_promotion = False
                    turn = functions.change_turn(turn)
                elif index == 2:
                    positionOfAllPieces = positionOfAllPieces[second_click_piece].Promotion(second_click_piece,positionOfAllPieces,2)
                    promotion_list_of_tiles = []
                    screen.blit(cleaning,(0,0))
                    flag_promotion = False
                    turn = functions.change_turn(turn)
                elif index == 3:
                    positionOfAllPieces = positionOfAllPieces[second_click_piece].Promotion(second_click_piece,positionOfAllPieces,3)
                    promotion_list_of_tiles = []
                    screen.blit(cleaning,(0,0))
                    flag_promotion = False
                    turn = functions.change_turn(turn)
    
    #highlight clicked cell
    if movesHighlightFlag:
        movement = positionOfAllPieces[first_click_index].move(first_click_index,positionOfAllPieces)
        for at in movement:
            move_pos = (Cells[at[0]][0],Cells[at[0]][1])
            screen.blit(highlight,move_pos)
        

    
    # PRINT THE BOARD BY FEN NOTATION
    piece_images = {
        "pawn": (bpawn, wpawn),
        "rook": (brook, wrook),
        "bishop": (bbishop, wbishop),
        "knight": (bknight, wknight),
        "queen": (bqueen, wqueen),
        "king": (bking, wking)
    }

    for index, piece in enumerate(positionOfAllPieces):
        if piece != "empty":
            screen.blit(piece_images[piece.name][piece.team], Cells[index])

    if result == 0:
        pass
    elif result == 1:
        font = pygame.font.SysFont("Arial", 50)
        if turn:
            txtsurf = font.render("Black Won",True, WHITE)
            screen.blit(txtsurf,(975, HEIGHT / 2))
        else:
            txtsurf = font.render("White Won",True, WHITE)
            screen.blit(txtsurf,(975, HEIGHT / 2))
    elif result == 2:
        font = pygame.font.SysFont("Arial", 50)
        txtsurf = font.render("Draw",True, WHITE)
        screen.blit(txtsurf,(1000, HEIGHT / 2))


    pygame.display.flip()
    Clock.tick(60)
