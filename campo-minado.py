class Posicao:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Identifica:
    def __init__(self, x, y simbolo)
    self.pos = Posicao(x, y)
    self.simbolo = simbolo

class Jogador:

    def __init__(self, x_inicial=0, y_inicial=0):
        self.pos = Posicao(x_inicial, y_inicial)
        self.simbolo = "B"

    def mover(self, mx, my):
        self.pos.x += mx
        self.pos.y += my

    def explodir(self, bum=False):
        if self.bum == True:          

    
#class Inimigo:

#class Bombas:
