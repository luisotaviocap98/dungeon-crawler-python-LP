import pygame
import labirinto
import sprites.fileload as SF
from random import randint, choice
# pylint: disable=no-member
# pylint: disable-msg=too-many-function-args

class Player:
    def __init__(self):
        self.xp = 0
        self.nivel = 0 
        self.sprite_atual = SF.playerDict[pygame.K_s] 
        self.stats = Stats(100,100,10,50,20,80)
        self.posicao_linha = 1
        self.posicao_coluna = 1
        
    def andar(self,direcao,mapa):
        if direcao == pygame.K_w and mapa.matriz[self.posicao_linha-1][self.posicao_coluna]!='*':
            self.posicao_linha -=1
            self.sprite_atual =SF.playerDict[direcao]

        elif direcao == pygame.K_a and mapa.matriz[self.posicao_linha][self.posicao_coluna-1]!='*':
            self.posicao_coluna -=1
            self.sprite_atual =SF.playerDict[direcao]
            
        elif direcao == pygame.K_s and mapa.matriz[self.posicao_linha+1][self.posicao_coluna]!='*':
            self.posicao_linha += 1
            self.sprite_atual =SF.playerDict[direcao]

        elif direcao == pygame.K_d and mapa.matriz[self.posicao_linha][self.posicao_coluna+1]!='*':
            self.posicao_coluna +=1
            self.sprite_atual = SF.playerDict[direcao]
    
    def desenhaPlayer(self):
        screen.blit(self.sprite_atual, (643+self.posicao_coluna*16,10+self.posicao_linha*16))
        
    def mostraStats(self):
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
    
class Mapa:
    def __init__(self, mapa, Y, X):
        self.matriz = mapa
        self.fog = None
        self.altura = Y
        self.largura = X
        
    
    def printMap(self):
        for i in range(0, len(self.matriz)):
            for j in range(0, len(self.matriz[i])):
                if self.matriz[i][j] != ' ':
                    screen.blit(SF.mapDict[self.matriz[i][j]], (640+j*16, 10+i*16))
                
    
class Stats:
    def __init__(self,lf, pw, cr, ds, ac, de):
        self.vida = lf
        self.power = pw
        self.critico= cr
        self.destreza= ds
        self.acuracia= ac
        self.defesa= de
'''
class Inventario:
    def __init__(self):
        self.armadura = Objeto()
        self.arma = Objeto()
        self.pocao = Objeto()

class Objeto:
    def __init__(self, nome):
        self.nome = nome
        self.stats = Stats()
'''   
class Inimigo:
    def __init__(self, img):
        self.stats = Stats(100,100,10,50,20,80)
        self.sprite = img
    

def modoCorre():
    screen.blit(modo_atual, (10,10))
    text1 = basicfont.render('W - cima', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render('S - baixo', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render('A - esquerda', True, (0, 0, 0), (255, 255, 255))
    text4 = basicfont.render('D - direita', True, (0, 0, 0), (255, 255, 255))

    screen.blit(text1, (50,500))
    screen.blit(text2, (50,530))
    screen.blit(text3, (50,560))
    screen.blit(text4, (50,590))
    
def modoSaida():
    screen.blit(modo_atual, (10,10))
    text3 = basicfont.render('Nivel finalizado', True, (0, 0, 0), (255, 255, 255))
    screen.blit(text3, (50,500))

def modoChest():
    screen.blit(modo_atual, (10,10))
    text1 = basicfont.render('bau encontrado', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render('C - abrir e pegar', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render('X - rejeitar', True, (0, 0, 0), (255, 255, 255))
    
    screen.blit(text1, (50,500))
    screen.blit(text2, (50,530))
    screen.blit(text3, (50,560))
    
def vectInimigo():
    Enemy = list()
    for i in range(1,7):
        Enemy.append(Inimigo(SF.inimigoDict[str(i)]))
    return Enemy

def verificaModo(mapa,x,y):
    return SF.modoDict[mapa.matriz[x][y]]   

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()
    done = False
    
    niveis = ['nivel1.txt','nivel2.txt','nivel3.txt']
    nivel_atual = 0
    #640 coluna 10 linha
    (map_bits,map_Y, map_X) = labirinto.carregaMap(niveis[nivel_atual])
    mapa = Mapa(map_bits,map_Y,map_X) 

    boneco = Player()
    
    inimigos = vectInimigo()
    
    modo_atual = verificaModo(mapa,boneco.posicao_linha,boneco.posicao_coluna)
       
    tecla_valida = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
    basicfont = pygame.font.SysFont(None, 30)
    
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
            
        screen.fill((255, 255, 255))#fundo da tela

        #modo a ser exibido
        if mapa.matriz[boneco.posicao_linha][boneco.posicao_coluna] == 'B':
            modoChest()
        elif mapa.matriz[boneco.posicao_linha][boneco.posicao_coluna] == 'S':
            modoSaida()
        else:
            modoCorre()
                
        boneco.mostraStats()
        #printando labirinto
        mapa.printMap()
                
        #teclas de movimento do personagem
        poll = pygame.event.poll
        event = poll()
        if event.type == pygame.KEYDOWN:
            boneco.andar(event.key,mapa)
            # if event.key in tecla_valida:
                # if randint(0,map_X*map_Y)/float(map_X*map_Y) > 0.95:
                    # E = choice(inimigos)
                    # print('modo batalha')
                    # screen.blit(E.sprite, (10,10))
                
        modo_atual = verificaModo(mapa,boneco.posicao_linha,boneco.posicao_coluna)
        #desenhando personagem
        boneco.desenhaPlayer()
        
        pygame.display.update()
        clock.tick(100)

