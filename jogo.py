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

class Game:
    def __init__(self):
        self.inimigos  = vectInimigo()
        self.jogador = Player()
        self.modo_atual = 'run'
        self.fase_atual = 0
        self.fases = ['fase1.txt','fase2.txt','fase3.txt']
        self.matriz_mapa = labirinto.carregaMap(self.fases[self.fase_atual])
        self.mapa = Mapa(self.matriz_mapa)

    def refreshTela(self):
        screen.fill((255, 255, 255))#fundo da tela
        self.mapa.printMap()
        self.jogador.desenhaPlayer()
        self.jogador.mostraStats()
        
    
    def moverPlayer(self,comando):
        if comando == pygame.K_w and self.mapa.matriz[self.jogador.posicao.x-1][self.jogador.posicao.y]!='*':
            self.jogador.salvaPosicaoAnterior()
            self.jogador.posicao.x -=1
            self.jogador.sprite_atual =SF.playerDict[comando]

        elif comando == pygame.K_a and self.mapa.matriz[self.jogador.posicao.x][self.jogador.posicao.y-1]!='*':
            self.jogador.salvaPosicaoAnterior()
            self.jogador.posicao.y -=1
            self.jogador.sprite_atual =SF.playerDict[comando]

        elif comando == pygame.K_s and self.mapa.matriz[self.jogador.posicao.x+1][self.jogador.posicao.y]!='*':
            self.jogador.salvaPosicaoAnterior()
            self.jogador.posicao.x +=1
            self.jogador.sprite_atual =SF.playerDict[comando]

        elif comando == pygame.K_d and self.mapa.matriz[self.jogador.posicao.x][self.jogador.posicao.y+1]!='*':
            self.jogador.salvaPosicaoAnterior()
            self.jogador.posicao.y +=1
            self.jogador.sprite_atual = SF.playerDict[comando]


    def inimigoEncontrado(self,comando,inimigo):
        if comando == pygame.K_x:
            print('atacando')
            self.batalhar(self.jogador, inimigo)
     
        elif comando == pygame.K_z:
            print('meteu pocao')
            self.usarPocao(self.jogador)


    def usarPocao(self,player):
        player.stats.vida +=1

    def batalhar(self,player,inimigo):
        
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


    def modoCorre(self,visao_atual):
        screen.blit(visao_atual, (10,10))
        text1 = basicfont.render('W - cima', True, (0, 0, 0), (255, 255, 255))
        text2 = basicfont.render('S - baixo', True, (0, 0, 0), (255, 255, 255))
        text3 = basicfont.render('A - esquerda', True, (0, 0, 0), (255, 255, 255))
        text4 = basicfont.render('D - direita', True, (0, 0, 0), (255, 255, 255))

        screen.blit(text1, (50,500))
        screen.blit(text2, (50,530))
        screen.blit(text3, (50,560))
        screen.blit(text4, (50,590))

    def modoSaida(self,visao_atual):
        screen.blit(visao_atual, (10,10))
        text3 = basicfont.render('Fase finalizada', True, (0, 0, 0), (255, 255, 255))
        screen.blit(text3, (50,500))

    def modoBau(self,visao_atual):
        screen.blit(visao_atual, (10,10))
        text1 = basicfont.render('Bau encontrado', True, (0, 0, 0), (255, 255, 255))
        text2 = basicfont.render('Conteudo do bau', True, (0, 0, 0), (255, 255, 255))

        screen.blit(text1, (50,500))
        screen.blit(text2, (50,530))

        bau = []
        altura = 0
        espada = randint(0,1)
        armadura = randint(0,1)
        pocoes = randint(0,3)
        # if randint(0,1) == 1:
        
        for i in bau:
            text1 = basicfont.render(i.nome, True, (0, 0, 0), (255, 255, 255))
            screen.blit(text1, (50,500+altura))
            altura+=30


    def modoInimigo(self,inimigo):
        screen.blit(inimigo.sprite, (10,10))
        text1 = basicfont.render('inimigo encontrado', True, (0, 0, 0), (255, 255, 255))
        text3 = basicfont.render('X - atacar', True, (0, 0, 0), (255, 255, 255))
        text5 = basicfont.render('Z - pocao', True, (0, 0, 0), (255, 255, 255))

        screen.blit(text1, (50,500))
        screen.blit(text3, (50,530))
        screen.blit(text5, (50,560))

    def changeModo(self):
        caracter = self.charPosicao()
        if self.modo_atual == 'run':
            self.modoCorre(SF.modoDict[caracter])
    
        elif self.modo_atual == 'bau':
            self.modoBau(SF.modoDict[caracter])

        elif self.modo_atual == 'saida':
            self.modoSaida(SF.modoDict[caracter])
        
        elif self.modo_atual == 'batalha':
            inimigo = self.inimigos[int(caracter) -1 ]
            self.modoInimigo(inimigo)

    def comandoValido(self, comando):
        caracter = self.charPosicao()
        
        if self.modo_atual == 'run':
            self.moverPlayer(comando)
            caracter = self.charPosicao()
            if caracter == 'B':
                self.modo_atual = 'bau'
            elif caracter.isnumeric():
                self.modo_atual = 'batalha'
            elif caracter == 'S':
                self.modo_atual = 'saida'
        
        elif self.modo_atual == 'bau':
            self.mapa.matriz[self.jogador.posicao.x][self.jogador.posicao.y] = ' '
            self.modo_atual = 'run'
        
        # elif modo_atual == 'saida':
        #     print('acabou')
        
        elif self.modo_atual == 'batalha':
            inimigo = self.inimigos[int(caracter) -1 ]
            self.inimigoEncontrado(comando, inimigo)
    
    def charPosicao(self):
        return self.mapa.matriz[self.jogador.posicao.x][self.jogador.posicao.y]
        

    
def vectInimigo():
    Enemy = list()
    for i in range(0,6):
        Enemy.append(Inimigo(SF.modoDict[str(i+1)]))
    return Enemy


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()
    done = False
    
    basicfont = pygame.font.SysFont(None, 25)
    
    game = Game()
    game.refreshTela()
    game.changeModo()
       
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                game.comandoValido(event.key)
                game.refreshTela()
                game.changeModo()
        
        pygame.display.update()
        clock.tick(50)

