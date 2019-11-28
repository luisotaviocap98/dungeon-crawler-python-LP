import pygame
# pylint: disable=no-member
# pylint: disable-msg=too-many-function-args
playerDict = {
    pygame.K_s :pygame.image.load('./sprites/personagem/bluedown3.png'),
    pygame.K_w: pygame.image.load('./sprites/personagem/bluebackwalk2.png'),
    pygame.K_a: pygame.image.load('./sprites/personagem/blueleftwalk2.png'),
    pygame.K_d: pygame.image.load('./sprites/personagem/bluerightwalk2.png')
}
mapDict = {
    'B':pygame.image.load('./sprites/bau/Treasure Chest closed 16x16.png'),
    '*':pygame.image.load('./sprites/parede/wall-16.png'),
    'S':pygame.image.load('./sprites/porta/fsmdoor.png'),
    '1':pygame.image.load('./sprites/inimigo/demonio16.png'),
    '2':pygame.image.load('./sprites/inimigo/disciple16.png'),
    '3':pygame.image.load('./sprites/inimigo/dorver-idle0-16.png'),
    '4':pygame.image.load('./sprites/inimigo/gnu16.png'),
    '5':pygame.image.load('./sprites/inimigo/mage-2-16.png'),
    '6':pygame.image.load('./sprites/inimigo/minotaur-b-axe1-16.png')
}

modoDict = {
    ' ':pygame.image.load('./sprites/modos/mode_R.png'),
    'B':pygame.image.load('./sprites/modos/mode_C.png'),
    'S':pygame.image.load('./sprites/modos/mode_D.png'),
    '1':pygame.image.load('./sprites/inimigo/vilao1.png'),
    '2':pygame.image.load('./sprites/inimigo/vilao2.png'),
    '3':pygame.image.load('./sprites/inimigo/vilao3.png'),
    '4':pygame.image.load('./sprites/inimigo/vilao4.png'),
    '5':pygame.image.load('./sprites/inimigo/vilao5.png'),
    '6':pygame.image.load('./sprites/inimigo/vilao6.png')
}
# inimigoDict = {
#     '1':pygame.image.load('./sprites/inimigo/vilao1.png'),
#     '2':pygame.image.load('./sprites/inimigo/vilao2.png'),
#     '3':pygame.image.load('./sprites/inimigo/vilao3.png'),
#     '4':pygame.image.load('./sprites/inimigo/vilao4.png'),
#     '5':pygame.image.load('./sprites/inimigo/vilao5.png'),
#     '6':pygame.image.load('./sprites/inimigo/vilao6.png')
# }