# CLASSE (O molde)
class Time: 
    # ATRIBUTO DE CLASSE (Contador na parede da fábrica)
    total_times = 0
    
    # MÉTODO (O verbo "nascer/construir")
    # 'nome' e 'divisao1' são PARÂMETROS (informações que chegam de fora)
    def __init__(self, nome, divisao): 
        # ATRIBUTOS DE INSTÂNCIA (A placa do carro)
        self.nome = nome       
        self.divisao = divisao
        Time.total_times += 1 

    def descricao(self):
        print(f'Olê, olê, olê, aqui é o {self.nome}.')

    def div(self):
        if self.divisao == True:
            print(f'Ão, ão, ão, é Primeira Divisão.')
        else:
            print(f'Olê, olê, olê, Primeira Divisão, cadê?')


# INSTÂNCIA / OBJETO (O carro construído e batizado de 'meu_time')
times = Time.total_times
print(f'Temos {times} times.')

time1 = Time("Bangu", False)
time2 = Time("Flamengo", True)
time3 = Time("Luizao", True)

# Chamando os métodos
time1.descricao()
time1.div()
print("-" * 30)

time2.descricao()
time2.div()
print("-" * 30)

time3.descricao()
time3.div()
print("-" * 30)

times = Time.total_times
print(f'Agora temos {times} times.')

    
    