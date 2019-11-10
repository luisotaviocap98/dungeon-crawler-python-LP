import pygame
import labirinto
from random import randint
# pylint: disable=no-member
# pylint: disable-msg=too-many-function-args

class Player:
    def __init__(self):
        self.xp = 0
        self.vida = 0 
        self.nivel = 0 
        self.stats = 0
        self.posicao_linha = 1
        self.posicao_coluna = 1
        
    def andar(self,direcao,mapa):
        if direcao == pygame.K_w and mapa.matriz[self.posicao_linha-1][self.posicao_coluna]!='*':
            self.posicao_linha -=1

        if direcao == pygame.K_a and mapa.matriz[self.posicao_linha][self.posicao_coluna-1]!='*':
            self.posicao_coluna -=1

        if direcao == pygame.K_s and mapa.matriz[self.posicao_linha+1][self.posicao_coluna]!='*':
            self.posicao_linha += 1

        if direcao == pygame.K_d and mapa.matriz[self.posicao_linha][self.posicao_coluna+1]!='*':
            self.posicao_coluna +=1
        
        return self.direcao(direcao)
        
    def direcao(self, direcao):
        if direcao == pygame.K_w:
            return pygame.image.load('./sprites/personagem/bluebackwalk2.png')
        if direcao == pygame.K_a:
            return pygame.image.load('./sprites/personagem/blueleftwalk2.png')
        if direcao == pygame.K_s:
            return pygame.image.load('./sprites/personagem/bluedown3.png')
        if direcao == pygame.K_d:
            return pygame.image.load('./sprites/personagem/bluerightwalk2.png')
 
class Mapa:
    def __init__(self, mapa, Y, X):
        self.matriz = mapa
        self.fog = None
        self.altura = Y
        self.largura = X
    
    
'''
class Stats:
    def __init__(self):
        self.power =0
        self.critico=0
        self.destreza=0
        self.acuracia=0
        self.defesa=0
    
        
class Inventario:
    def __init__(self):
        self.armadura = Objeto()
        self.arma = Objeto()
        self.pocao = Objeto()

class Objeto:
    def __init__(self, nome):
        self.nome = nome
        self.stats = Stats()

    
class Inimigo:
    def __init__(self):
        self.vida=0
        self.power =0
        self.stats=0
    
'''

if __name__ == '__main__':
    #640 coluna 10 linha
    mapa = Mapa(labirinto.carregaMap()[0],labirinto.carregaMap()[1],labirinto.carregaMap()[2]) 
    boneco = Player()
   
    parede = pygame.image.load('./sprites/parede/wall-16.png')
    chao = pygame.image.load('./sprites/chao/grama.png')
    bau = pygame.image.load('./sprites/bau/Treasure Chest closed 16x16.png')
    porta = pygame.image.load('./sprites/porta/fsmdoor.png')
    modoRun = pygame.image.load('./sprites/modos/mode_R.png')
    modoBau = pygame.image.load('./sprites/modos/mode_C.png')
    modoPorta = pygame.image.load('./sprites/modos/mode_D.png')
    personagem = pygame.image.load('./sprites/personagem/bluedown3.png')
    inimigo = pygame.image.load('./sprites/inimigo/vilao2.png')
    
    
    pygame.init()
    screen = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()
    done = False
       
    modo_atual = 'run'
    tecla_valida = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
            
        screen.fill((255, 255, 255))

        

        basicfont = pygame.font.SysFont(None, 30)
        #modo a ser exibido
        if mapa.matriz[boneco.posicao_linha][boneco.posicao_coluna] == 'B':
            screen.blit(modoBau, (10,10))
            text1 = basicfont.render('bau encontrado', True, (0, 0, 0), (255, 255, 255))
            
            text2 = basicfont.render('C - abrir e pegar', True, (0, 0, 0), (255, 255, 255))
            text3 = basicfont.render('X - rejeitar', True, (0, 0, 0), (255, 255, 255))
            

            screen.blit(text3, (50,560))

            screen.blit(text2, (50,530))
            screen.blit(text1, (50,500))
           
          
        elif mapa.matriz[boneco.posicao_linha][boneco.posicao_coluna] == 'S':
            screen.blit(modoPorta, (10,10))
        else:
            screen.blit(modoRun, (10,10))
            #textos explicativos
            text1 = basicfont.render('W - cima', True, (0, 0, 0), (255, 255, 255))
            text2 = basicfont.render('S - baixo', True, (0, 0, 0), (255, 255, 255))
            text3 = basicfont.render('A - esquerda', True, (0, 0, 0), (255, 255, 255))
            text4 = basicfont.render('D - direita', True, (0, 0, 0), (255, 255, 255))

            screen.blit(text1, (50,500))
            screen.blit(text2, (50,530))
            screen.blit(text3, (50,560))
            screen.blit(text4, (50,590))
            
                
            
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
                
        #printando labirinto
        for i in range(0, len(mapa.matriz)):
            for j in range(0, len(mapa.matriz[i])):
                if mapa.matriz[i][j] == '*':
                    screen.blit(parede, (640+j*16, 10+i*16))
                elif mapa.matriz[i][j] == 'B':
                    screen.blit(bau,(640+j*16, 10+i*16))
                elif mapa.matriz[i][j] == 'S':
                    screen.blit(porta,(640+j*16, 10+i*16))
                
        #teclas de movimento do personagem
        poll = pygame.event.poll
        event = poll()
        if event.type == pygame.KEYDOWN:
            if randint(0,100) > 95:
                print('modo batalha')
            if event.key in tecla_valida:
                personagem =boneco.andar(event.key,mapa)
        
        
        #desenhando personagem
        screen.blit(personagem, (643+boneco.posicao_coluna*16,10+boneco.posicao_linha*16))
        
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(100)
#ideia pra pegar posicao, exemplo se for matriz de 32 linha x 32 coluna, posicao é x = n * 32 , y = n * 32, 
# conforme o personagem anda aumenta/diminui x e y
