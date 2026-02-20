class Pessoa:
    # Método construtor (inicializador)
    def __init__(self, nome, idade):
        self.nome = nome    # Atributo de instância
        self.idade = idade  # Atributo de instância

    # Método (comportamento)
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Instanciando (criando o objeto)
p1 = Pessoa("Maria", 25)
print(p1.apresentar())