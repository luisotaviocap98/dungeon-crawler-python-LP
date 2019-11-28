import pygame
import labirinto
import sprites.fileload as SF
from random import randint, choice
# pylint: disable=no-member
# pylint: disable-msg=too-many-function-args

class Posicao:
    def __init__(self):
        self.x = 1
        self.y = 1

class Player:
    def __init__(self):
        self.xp = 0
        self.nivel = 0 
        self.posicao = Posicao()
        self.old_posicao = Posicao()
        self.stats = Stats(100,100,10,50,20,80)
        self.sprite_atual = SF.playerDict[pygame.K_s] 
    
    def salvaPosicaoAnterior(self):
        self.old_posicao.x, self.old_posicao.y = self.posicao.x, self.posicao.y
    
    def retornaPosicaoAnterior(self):
        self.posicao.x, self.posicao.y = self.old_posicao.x, self.old_posicao.y 

    def desenhaPlayer(self):
        screen.blit(self.sprite_atual, (643+self.posicao.y*16,10+self.posicao.x*16))
        
    def mostraStats(self):
        textf = basicfont.render('forca:'+str(self.stats.forca), True, (0, 0, 0), (255, 255, 255))
        textd = basicfont.render('defesa:'+str(self.stats.defesa), True, (0, 0, 0), (255, 255, 255))
        texta = basicfont.render('acuracia:'+str(self.stats.acuracia), True, (0, 0, 0), (255, 255, 255))
        texth = basicfont.render('destreza:'+str(self.stats.destreza), True, (0, 0, 0), (255, 255, 255))
        textc = basicfont.render('critico:'+str(self.stats.critico), True, (0, 0, 0), (255, 255, 255))

        screen.blit(textf, (650,500))
        screen.blit(textd, (650,530))
        screen.blit(texta, (650,560))
        screen.blit(texth, (650,590))
        screen.blit(textc, (650,620))
    
class Inimigo:
    def __init__(self, img):
        self.stats = Stats(100,100,10,50,20,80)
        self.sprite = img

class Mapa:
    def __init__(self, mapa):
        self.matriz = mapa
        self.fog = None

    def printMap(self):
        for i in range(0, len(self.matriz)):
            for j in range(0, len(self.matriz[i])):
                if self.matriz[i][j] != ' ' and not (self.matriz[i][j]).isnumeric():
                    screen.blit(SF.mapDict[self.matriz[i][j]], (640+j*16, 10+i*16))
    
class Stats:
    def __init__(self,vida, forca, critico, destreza, acuracia, defesa):
        self.vida = vida
        self.forca = forca
        self.defesa= defesa
        self.critico= critico
        self.destreza= destreza
        self.acuracia= acuracia
        
class Objeto:
    def __init__(self,nome):
        self.nome = nome
        self.atributos = Stats(100,50,20,10,30,80)

'''
class Inventario:
    def __init__(self):
        self.armadura = Objeto()
        self.arma = Objeto()
        self.pocao = Objeto()
'''

def gerador_de_objetos():
    bau = []
    espada = Objeto('espada') 
    armadura = Objeto('armadura')
    pocao = Objeto('bruxaria')
    bau.append(espada)
    bau.append(armadura)
    bau.append(pocao)
    return bau
     

def moverPlayer(jogador,comando,mapa):
    if comando == pygame.K_w and mapa.matriz[jogador.posicao.x-1][jogador.posicao.y]!='*':
        jogador.salvaPosicaoAnterior()
        jogador.posicao.x -=1
        jogador.sprite_atual =SF.playerDict[comando]

    elif comando == pygame.K_a and mapa.matriz[jogador.posicao.x][jogador.posicao.y-1]!='*':
        jogador.salvaPosicaoAnterior()
        jogador.posicao.y -=1
        jogador.sprite_atual =SF.playerDict[comando]
        
    elif comando == pygame.K_s and mapa.matriz[jogador.posicao.x+1][jogador.posicao.y]!='*':
        jogador.salvaPosicaoAnterior()
        jogador.posicao.x +=1
        jogador.sprite_atual =SF.playerDict[comando]

    elif comando == pygame.K_d and mapa.matriz[jogador.posicao.x][jogador.posicao.y+1]!='*':
        jogador.salvaPosicaoAnterior()
        jogador.posicao.y +=1
        jogador.sprite_atual = SF.playerDict[comando]

     
def bauEncontrado(jogador,comando,mapa):
    if comando == pygame.K_c:
        print('pegou')
        mapa.matriz[jogador.posicao.x][jogador.posicao.y] = ' '
        # return 'P'
    elif comando == pygame.K_x:
        print('rejeitou')
        jogador.retornaPosicaoAnterior()
        

def inimigoEncontrado(jogador,comando,inimigo):
    if comando == pygame.K_b:
        print('batalhando')
        batalhar(jogador, inimigo)
    elif comando == pygame.K_x:
        print('fugiu')
        jogador.retornaPosicaoAnterior()
    elif comando == pygame.K_z:
        print('meteu pocao')

        
def batalhar(player,inimigo):
    # player.stats.forca 
    # inimigos[int(mapa.matriz[player.posicao.x][player.posicao.y]) -1 ].stats.forca 
    if inimigo.stats.destreza < player.stats.acuracia:
        print('consegue atacar')
    if inimigo.stats.destreza > player.stats.acuracia:
        print('nao acertou inimigo')
    if inimigo.stats.acuracia < player.stats.destreza:
        print('inimigo errou ataque')
    if inimigo.stats.acuracia > player.stats.destreza:
        print('inimigo te atingiu')
    if inimigo.stats.vida ==0 :
        print('venceu inimigo')
    if player.stats.vida ==0 : 
        print('voce morreu')
        

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
    text3 = basicfont.render('Fase finalizado', True, (0, 0, 0), (255, 255, 255))
    screen.blit(text3, (50,500))

def modoBau(modo_atual):
    screen.blit(modo_atual, (10,10))
    text1 = basicfont.render('bau encontrado', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render('C - abrir e pegar', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render('X - rejeitar', True, (0, 0, 0), (255, 255, 255))
    
    screen.blit(text1, (50,500))
    screen.blit(text2, (50,530))
    screen.blit(text3, (50,560))
    
def abrirBau(bau):
    text1 = basicfont.render('Conteudo do bau', True, (0, 0, 0), (255, 255, 255))
    screen.blit(text1, (50,500))
    altura = 0
    for i in bau:
        text1 = basicfont.render(i.nome, True, (0, 0, 0), (255, 255, 255))
        screen.blit(text1, (50,500+altura))
        altura+=30
    
    
def modoInimigo(inimigo):
    screen.blit(inimigo.sprite, (10,10))
    text1 = basicfont.render('inimigo encontrado', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render('B - batalhar', True, (0, 0, 0), (255, 255, 255))
    text4 = basicfont.render('X - fugir', True, (0, 0, 0), (255, 255, 255))
    text5 = basicfont.render('Z - pocao', True, (0, 0, 0), (255, 255, 255))
    
    screen.blit(text1, (50,500))
    screen.blit(text3, (50,530))
    screen.blit(text4, (50,560))
    screen.blit(text5, (50,590))
    
def changeModo(caracter,modo_atual):
    if caracter == ' ':
        modoCorre(modo_atual)
    elif caracter == 'B':
        modoBau(modo_atual)
    elif caracter == 'S':
        modoSaida(modo_atual)
    elif caracter.isnumeric():
        inimigo = inimigos[int(caracter) -1 ]
        modoInimigo(inimigo)

def comandoValido(caracter,jogador, comando, mapa):
    if caracter == ' ':
        moverPlayer(jogador,comando,mapa)
    elif caracter == 'B':
        bauEncontrado(jogador,comando,mapa)
    elif caracter == 'S':
        print('acabou')
    elif caracter.isnumeric():
        inimigo = inimigos[int(caracter) -1 ]
        inimigoEncontrado(jogador,comando,inimigo)

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
    
    fases = ['fase1.txt','fase2.txt','fase3.txt']
    fase_atual = 0
    #640 coluna 10 linha
    map_bits = labirinto.carregaMap(fases[fase_atual])
    mapa = Mapa(map_bits) 

    player = Player()
    
    inimigos = vectInimigo()
       
    basicfont = pygame.font.SysFont(None, 25)
    
    screen.fill((255, 255, 255))#fundo da tela
    mapa.printMap()
    player.desenhaPlayer()
    player.mostraStats()
    charCoordenada = mapa.matriz[player.posicao.x][player.posicao.y]
    modo_atual = verificaModo(charCoordenada)
    changeModo(charCoordenada,modo_atual)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
            
                comandoValido(charCoordenada,player,event.key,mapa)
                screen.fill((255, 255, 255))#fundo da tela
                        
                mapa.printMap()
                player.desenhaPlayer()
                player.mostraStats()
                charCoordenada = mapa.matriz[player.posicao.x][player.posicao.y]
                modo_atual = verificaModo(charCoordenada)
                changeModo(charCoordenada,modo_atual)
        
        pygame.display.update()
        clock.tick(50)

