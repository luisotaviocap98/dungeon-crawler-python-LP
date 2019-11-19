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
        self.col_anterior = 1
        self.lin_anterior = 1
        
    def andar(self,direcao):
        if direcao == pygame.K_w and mapa.matriz[self.posicao_linha-1][self.posicao_coluna]!='*':
            self.salvaPosicaoAnterior()
            self.posicao_linha -=1
            self.sprite_atual =SF.playerDict[direcao]

        elif direcao == pygame.K_a and mapa.matriz[self.posicao_linha][self.posicao_coluna-1]!='*':
            self.salvaPosicaoAnterior()
            self.posicao_coluna -=1
            self.sprite_atual =SF.playerDict[direcao]
            
        elif direcao == pygame.K_s and mapa.matriz[self.posicao_linha+1][self.posicao_coluna]!='*':
            self.salvaPosicaoAnterior()
            self.posicao_linha += 1
            self.sprite_atual =SF.playerDict[direcao]

        elif direcao == pygame.K_d and mapa.matriz[self.posicao_linha][self.posicao_coluna+1]!='*':
            self.salvaPosicaoAnterior()
            self.posicao_coluna +=1
            self.sprite_atual = SF.playerDict[direcao]
    
    def salvaPosicaoAnterior(self):
        self.col_anterior = self.posicao_coluna 
        self.lin_anterior = self.posicao_linha 
    
    def retornaPosicaoAnterior(self):
        self.posicao_coluna = self.col_anterior
        self.posicao_linha = self.lin_anterior

    def findBau(self,comando):
        if comando == pygame.K_c:
            print('pegou')
            mapa.matriz[self.posicao_linha][self.posicao_coluna] = ' '
        elif comando == pygame.K_x:
            print('rejeitou')
            self.retornaPosicaoAnterior()
    
    def combate(self,comando):
        if comando == pygame.K_z:
            print('batalhando')
        elif comando == pygame.K_x:
            print('fugiu')
            self.retornaPosicaoAnterior()
        elif comando == pygame.K_c:
            print('meteu pocao')
                        
    def comandoValido(self, modo):
        if modo == ' ':
            self.andar(event.key)
        elif modo == 'B':
            self.findBau(event.key)
        elif modo.isnumeric():
            self.combate(event.key)
        # elif modo == 'S':
            

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
                if self.matriz[i][j] != ' ' and not (self.matriz[i][j]).isnumeric():
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
    

def modoCorre(modo_atual):
    screen.blit(modo_atual, (10,10))
    text1 = basicfont.render('W - cima', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render('S - baixo', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render('A - esquerda', True, (0, 0, 0), (255, 255, 255))
    text4 = basicfont.render('D - direita', True, (0, 0, 0), (255, 255, 255))

    screen.blit(text1, (50,500))
    screen.blit(text2, (50,530))
    screen.blit(text3, (50,560))
    screen.blit(text4, (50,590))
    
def modoSaida(modo_atual):
    screen.blit(modo_atual, (10,10))
    text3 = basicfont.render('Nivel finalizado', True, (0, 0, 0), (255, 255, 255))
    screen.blit(text3, (50,500))
    # mudarNivel(nivel)

def mudarNivel(nivel_atual):
    nivel_atual +=1

def modoChest(modo_atual):
    screen.blit(modo_atual, (10,10))
    text1 = basicfont.render('bau encontrado', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render('C - abrir e pegar', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render('X - rejeitar', True, (0, 0, 0), (255, 255, 255))
    
    screen.blit(text1, (50,500))
    screen.blit(text2, (50,530))
    screen.blit(text3, (50,560))
    
def modoInimigo(charPos):
    screen.blit(inimigos[int(charPos) -1 ].sprite, (10,10))
    text1 = basicfont.render('inimigo encontrado', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render('poder:'+str(inimigos[int(charPos)-1].stats.power), True, (0, 0, 0), (255, 255, 255))
    
    screen.blit(text1, (50,500))
    screen.blit(text2, (50,530))
    
def changeModo(caracter,modo_atual):
    if caracter == ' ':
        modoCorre(modo_atual)
    elif caracter == 'B':
        modoChest(modo_atual)
    elif caracter == 'S':
        modoSaida(modo_atual)
    elif caracter.isnumeric():
        modoInimigo(caracter)


def vectInimigo():
    Enemy = list()
    for i in range(0,6):
        Enemy.append(Inimigo(SF.modoDict[str(i+1)]))
    return Enemy

def verificaModo(bit):
    return SF.modoDict[bit]   

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
       
    basicfont = pygame.font.SysFont(None, 25)
    
    screen.fill((255, 255, 255))#fundo da tela
    mapa.printMap()
    boneco.desenhaPlayer()
    boneco.mostraStats()
    charCoordenada = mapa.matriz[boneco.posicao_linha][boneco.posicao_coluna]
    modo_atual = verificaModo(charCoordenada)
    changeModo(charCoordenada,modo_atual)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
               
                screen.fill((255, 255, 255))#fundo da tela
                mapa.printMap()
        
                #modo a ser exibido
                # if charCoordenada == 'B':
                    # modoChest()
                # elif charCoordenada == 'S':
                    # modoSaida(nivel_atual)
                # elif charCoordenada.isnumeric():
                    # modoInimigo(charCoordenada)
                # else:
                    # modoCorre()
                        
                boneco.comandoValido(charCoordenada)
                boneco.desenhaPlayer()
                boneco.mostraStats()
                charCoordenada = mapa.matriz[boneco.posicao_linha][boneco.posicao_coluna]
                modo_atual = verificaModo(charCoordenada)
                changeModo(charCoordenada,modo_atual)
        
        pygame.display.update()
        clock.tick(50)

