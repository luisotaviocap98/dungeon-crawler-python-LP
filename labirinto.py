import pygame
# pylint: disable=no-member
# pylint: disable-msg=too-many-function-args

class Player:
    def __init__(self):
        self.xp = 0
        self.vida = 0 
        self.nivel = 0 
        self.status = 0
        self.posicao_linha = 0 
        self.posicao_coluna = 0
        
    def andar(self,direcao):
        if direcao == 'direita':
            self.posicao_coluna +=1
            
        if direcao == 'esquerda':
            self.posicao_coluna -=1
            
        if direcao == 'baixo':
            self.posicao_linha += 1
        
        if direcao == 'cima':
            self.posicao_linha -=1
            
        
''' 
class Mapa:
    def __init__(self):
        self.matriz
        self.fog
    
class Status:
    def __init__(self):
        self.power
        self.critico
        self.destreza
        self.acuracia
        self.defesa
    
class Cena:
    def __init__(self):
        self.inimigo
        self.bau
        self.paredes
        self.text
class Inventario:
    def __init__(self):
        self.armadura
        self.arma 

class Labirinto:
    def __init__(self):
        self.size_x
        self.size_y 
        self.inimigos
        self.niveis
        self.cena
    
class Inimigo:
    def __init__(self):
        self.vida
        self.power 
        self.posicao 
        self.status
    
    
class Batalha:
    def __init__(self):
        self.player
        self.inimigo
    
'''
#criador de labrinto    
from random import shuffle, randrange
 
def make_maze(w = 16, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [['*  '] * w + ['*'] for _ in range(h)] + [[]]
    hor = [['***'] * w + ['*'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = '*  '
            if yy == y: ver[y][max(x, xx)] = '   '
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s
 
if __name__ == '__main__':
    '''
    lab = make_maze(10,10)
    f = open('nivel1.txt','w')
    f.write(lab)
    f.close()
    lab = make_maze(12,12)
    f = open('nivel2.txt','w')
    f.write(lab)
    f.close()
    lab = make_maze(14,14)
    f = open('nivel3.txt','w')
    f.write(lab)
    f.close()
    '''
    linha = list()
    j = open('nivel2.txt','r')
    cont =0 
    for i in j.readlines():
        coluna = list()
        f = i.split('\n')
        cont +=1
        cont2 =0
         
        for k in f[0]:
            cont2+=1
            coluna.append(k)
        linha.append(coluna.copy())
        coluna.clear()
    
    #    if k == '*':
    #            print('[{},{}]'.format(cont,cont2),end=' ')
    #    print()
    #print(linha[0][0])
    #j.close()
   
    image = pygame.image.load('./sprites/parede/wall-16.png')
    bau = pygame.image.load('./sprites/bau/Treasure Chest closed 16x16.png')
    porta = pygame.image.load('./sprites/porta/fsmdoor.png')
    modoRun = pygame.image.load('./sprites/modos/mode_R.png')
    
    window = (16,16)
    background = pygame.Surface(window)
    pygame.draw.rect(background,(1,1,1),(0,0,1,1))
    
    
    pygame.init()
    screen = pygame.display.set_mode((1280, 640))
    done = False
    clock = pygame.time.Clock()
       
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill((255, 255, 255))

        basicfont = pygame.font.SysFont(None, 30)
        text1 = basicfont.render('W - cima', True, (0, 0, 0), (255, 255, 255))
        text2 = basicfont.render('S - baixo', True, (0, 0, 0), (255, 255, 255))
        text3 = basicfont.render('A - esquerda', True, (0, 0, 0), (255, 255, 255))
        text4 = basicfont.render('D - direita', True, (0, 0, 0), (255, 255, 255))

        textf = basicfont.render('forca:     100', True, (0, 0, 0), (255, 255, 255))
        textd = basicfont.render('defesa:    200', True, (0, 0, 0), (255, 255, 255))
        texta = basicfont.render('acuracia:  50', True, (0, 0, 0), (255, 255, 255))
        texth = basicfont.render('destreza:  10', True, (0, 0, 0), (255, 255, 255))
        textc = basicfont.render('critico:   30', True, (0, 0, 0), (255, 255, 255))

        screen.blit(textf, (650,500))
        screen.blit(textd, (650,530))
        screen.blit(texta, (650,560))
        screen.blit(texth, (650,590))
        screen.blit(textc, (650,620))

        screen.blit(text1, (50,500))
        screen.blit(text2, (50,530))
        screen.blit(text3, (50,560))
        screen.blit(text4, (50,590))
        
        screen.blit(modoRun, (10,10))

        for i in range(0, len(linha)):
            for j in range(0, len(linha[i])):
                if linha[i][j] == '*':
                    screen.blit(image, (640+j*16, 10+i*16))
                # elif linha[i][j] == ' ':
                #     screen.blit(background,(640+j*16, 10+i*16))
                elif linha[i][j] == 'B':
                    screen.blit(bau,(640+j*16, 10+i*16))
                elif linha[i][j] == 'S':
                    screen.blit(porta,(640+j*16, 10+i*16))
                    
        pygame.display.flip()
        clock.tick(60)
#ideia pra pegar posicao, exemplo se for matriz de 32 linha x 32 coluna, posicao é x = n * 32 , y = n * 32, 
# conforme o personagem anda aumenta/diminui x e y
