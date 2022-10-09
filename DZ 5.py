# # #Создайте программу для игры в ""Крестики-нолики"".


# import pygame
# import sys

# def check_win(max,sign):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sign) == 3:
#             return sign
#     for col in range(3):
#         if mas[0][col]== sign and mas[1][col]== sign and mas[2][col]:
#             return sign
#     if mas[0][0]== sign and mas[1][1]== sign and mas[2][2]:
#         return sign   
#     if mas[0][2]== sign and mas[1][1]== sign and mas[2][0]:
#         return sign   
#     if zeroes == 0:
#         return 'Piece'   
#     return False

# pygame.init()
# size_block = 100
# margin = 15
# width = heigth = size_block * 3 + margin * 4

# size_window = (width, heigth)
# screen = pygame.display.set_mode(size_window)
# pygame.display.set_caption("Крестики-нолики")

# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)
# white = (255,255,255)
# mas = [[0]*3 for i in range(3)]
# query = 0
# game_over = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit(0)
#         elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             x_mouse, y_mouse = pygame.mouse.get_pos()
#             col = x_mouse//(size_block+margin)
#             row = y_mouse//(size_block+margin)
#             if mas[row][col] == 0:
#                 if query%2 ==0:
#                     mas[row][col] = 'x'
#                 else:
#                     mas[row][col] = 'o'
#                 query +=1
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             game_over = False
#             mas = [[0]*3 for i in range(3)]
#             query = 0
#             screen.fill(black)

#     if not game_over:
#         for row in range(3):
#             for col in range(3):
#                 if mas[row][col] == 'x':
#                     color = red
#                 elif mas[row][col] == 'o':
#                     color = green
#                 else:
#                     color = white
#                 x = col*size_block + (col+1)*margin
#                 y = row*size_block + (row+1)* margin
#                 pygame.draw.rect(screen,color,(x,y,size_block,size_block))
#                 if color == red:
#                     pygame.draw.line(screen,white, (x+5,y+5),(x+size_block-5,y+size_block-5),3)
#                     pygame.draw.line(screen,white, (x+size_block-5,y+5),(x+5,y+size_block-5),3)
#                 elif color == green:
#                     pygame.draw.circle(screen,white,(x+size_block//2,y+size_block//2),size_block//2-3,3)
#     if (query-1)%2 == 0:
#         game_over = check_win(mas, 'x')
#     else:
#         game_over = check_win(mas, 'x')
    
#     if game_over:
#         screen.fill(black)
#         font = pygame.font.SysFont('stxingkai',80)
#         text1 = font.render(game_over, True,white)
#         text_rect = text1.get_rect()
#         text_x = screen.get_width()/2 - text_rect.width/2
#         text_y = screen.get_height()/2 - text_rect.height/2
#         screen.blit(text1,[text_x,text_y])


#     pygame.display.update()



doska = list(range(1,10))

def draw_board(board):

 for i in range(3):
     print ("|", doska[0+i*3], "|", doska[1+i*3], "|",doska[2+i*3], "|")

def stavim_hod(hod):
 valid = False
 while not valid:
     otvet = input("Введите номер клетки куда поставить значение " + hod+"? ")
     otv = int(otvet)
     if otv >= 1 and otv <= 9:
         if (str(doska[otv-1]) not in "XO"):
             doska[otv-1] = hod
             valid = True
         else:
             print ("Эта клетка занята")
def kto_viigral(doska):
 pobeda = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
 for x in pobeda:
     if doska[x[0]] == doska[x[1]] == doska[x[2]]:
         return doska[x[0]]
 return False

def igra(doska):
 count = 0
 win = False
 while not win:
     draw_board(doska)
     if count % 2 == 0:
         stavim_hod("X")
     else:
         stavim_hod("O")
     count += 1
     if count > 4:
         m = kto_viigral(doska)
         if m:
             print (m, "Победил!")
             win = True
             break
     if count == 9:
         print ("Победила дружба!")
         break
 draw_board(doska)

igra(doska)