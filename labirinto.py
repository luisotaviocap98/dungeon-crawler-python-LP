class Player:
    self.vida
    self.power
    
class Inventario:
    self.armadura
    self.arma 
    
class Labirinto:
    self.size_x
    self.size_y 
    self.posicao_player
    self.inimigos
    self.niveis
    
class Inimigo:
    self.vida
    self.power 
    self.posicao 
    
#ideia pra pegar posicao, exemplo se for matriz de 32 linha x 32 coluna, posicao é x = n * 32 , y = n * 32, 
# conforme o personagem anda aumenta/diminui x e y