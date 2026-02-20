import math

class Circulo:
    # 1. Método construtor com valores padrão definidos nos parâmetros
    def __init__(self, x=0, y=0, raio=1):
        # Vê se o raio é válido
        if raio < 0:
            raise ValueError("Raio não pode ser valor negativo.")    
        
        # Atribui os valores recebidos aos atributos definidos no __init__
        self.x = x      
        self.y = y    
        self.raio = raio

    # Método Area
    def area(self):
        return math.pi * (self.raio**2)
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def contem(self, px, py):
        distancia = math.sqrt((self.x - px)**2 + (self.y - py)**2)
        if distancia <= self.raio:
            return True
        else:
            return False


# Instanciando (criando) o objeto

meu_circulo = Circulo(2, 3, 5) # Cria um objeto "meu_circulo" com os valores de x, y, raio atualizados.

resultado_area = meu_circulo.area() # Usa os parâmetros do objeto "meu_circulo" para realizar o método "area"
resultado_perimetro = meu_circulo.perimetro()
print(f'Meu círculo tem um x={meu_circulo.x}, um y={meu_circulo.y} e raio={meu_circulo.raio}') 
print(f"A área do círculo é {resultado_area:.2f}")
print(f'Perímetro: {resultado_perimetro:.2f}')
print("-" * 30)

print(f'Centro: X={meu_circulo.x}, Y={meu_circulo.y}.\nMovendo 10 no x e 5 no y...')
meu_circulo.mover(10, 5)
print(f"Novo centro: X={meu_circulo.x}, Y={meu_circulo.y}")
print("-" * 30)

ponto_dentro = meu_circulo.contem(13, 9)
ponto_fora = meu_circulo.contem(100, 100)

print(f"O ponto (13, 9) está dentro? {ponto_dentro}")
print(f"O ponto (100, 100) está dentro? {ponto_fora}")
