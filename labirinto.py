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
    j = open('nivel1.txt','r')
    cont =0 
    for i in j.readlines():
        coluna = list()
        f = i.split('\n')
        cont +=1
        cont2 =0 
        for k in f[0]:
            cont2+=1
            coluna.append(k)
            if k == '*':
                print('[{},{}]'.format(cont,cont2),end=' ')
        print()
        linha.append(coluna.copy())
        coluna.clear()
    print(linha)
#ideia pra pegar posicao, exemplo se for matriz de 32 linha x 32 coluna, posicao é x = n * 32 , y = n * 32, 
# conforme o personagem anda aumenta/diminui x e y
