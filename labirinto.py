#criador de labrinto    
from random import shuffle, randrange
def make_maze(w = 16, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [['* '] * w + ['*'] for _ in range(h)] + [[]]
    hor = [['**'] * w + ['*'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = '* '
            if yy == y: ver[y][max(x, xx)] = '  '
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s
 
def createMaze():
    lab = make_maze(18,13)
    f = open('nivel1.txt','w')
    f.write(lab)
    f.close()
    
    lab = make_maze(18,13)
    f = open('nivel2.txt','w')
    f.write(lab)
    f.close()
    
    lab = make_maze(18,13)
    f = open('nivel3.txt','w')
    f.write(lab)
    f.close()
    

def carregaMap(arq):
    linha = list()
    arquivo = open(arq,'r')
    for i in arquivo.readlines():
        coluna = list()
        caracteres = i.split('\n')
         
        for j in caracteres[0]:
            coluna.append(j)
        linha.append(coluna.copy())
        coluna.clear()
    arquivo.close()
    
    return linha
    
if __name__ == '__main__':
    createMaze()
