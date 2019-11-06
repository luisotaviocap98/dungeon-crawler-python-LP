'''class Player:
    self.vida
    self.xp
    self.nivel
    self.status
    self.posicao_player
    
class Status:
    self.power
    self.critico
    self.destreza
    self.acuracia
    self.defesa
    
class Cena:
    self.inimigo
    self.bau
    self.paredes
    self.text
class Inventario:
    self.armadura
    self.arma 
    
class Labirinto:
    self.size_x
    self.size_y 
    self.inimigos
    self.niveis
    self.cena
    
class Inimigo:
    self.vida
    self.power 
    self.posicao 
    self.status
    
    
class Batalha:
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
    
    
    j = open('nivel1.txt','r')
    cont =0 
    for i in j.readlines():
        f = i.split('\n')
        cont +=1
        cont2 =0 
        for k in f[0]:
            cont2+=1
            if k == '*':
                print('[{},{}]'.format(cont,cont2),end=' ')
        print()
    
#ideia pra pegar posicao, exemplo se for matriz de 32 linha x 32 coluna, posicao é x = n * 32 , y = n * 32, 
# conforme o personagem anda aumenta/diminui x e y
