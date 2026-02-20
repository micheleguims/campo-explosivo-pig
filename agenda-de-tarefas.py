class Tarefa:

    def __init__(self, titulo, prioridade, concluida = False):
        if prioridade < 1 or prioridade > 5:
            raise ValueError("Prioridade vai de 1 a 5")
        self.titulo = titulo
        self.prioridade = prioridade
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def reabrir(self):
        self.concluida = False
        
    def descricao(self):
        status = "✅" if self.concluida else "❌"
        return f"Tarefa: {self.titulo} | Prioridade: {self.prioridade} | Status: {status}"

# Instanciando o objeto

t1 = Tarefa("Rodar esse código", 5)
print(t1.descricao())

t1.concluir()

print(t1.descricao())

class Agenda:
    
    def __init__(self):
        self.listaTarefas = []

    def adicionar(self, obj_tarefa):
        self.listaTarefas.append(obj_tarefa)

    def remover(self, titulo):
        for i in self.listaTarefas:
            if i.titulo == titulo:
                self.listaTarefas.remove(i)
                return
        else:
            raise LookupError("Tarefa não encontrada.")
        
    def listar(self, apenas_pendentes = False):
        mostrar_lista = []

        for i in self.listaTarefas:
            if not apenas_pendentes or not i.concluida:
                mostrar_lista.append(i.descricao())
        return mostrar_lista
    
    def buscar(self, trecho):
        busca_trecho = []

        for i in self.listaTarefas:
            if trecho.lower() in i.titulo.lower():
                busca_trecho.append(i.descricao())
        return busca_trecho


#### ---------------------------------- ####

# --- Testando sua Implementação ---
try:
    minha_agenda = Agenda()
    
    # Criando as tarefas
    t1 = Tarefa("Estudar Estrutura de Dados", 5)
    t2 = Tarefa("Fazer AD1 de Matemática", 4)
    t3 = Tarefa("Revisar Física", 3)
    
    # Adicionando na agenda
    minha_agenda.adicionar(t1)
    minha_agenda.adicionar(t2)
    minha_agenda.adicionar(t3)
    
    # Concluindo uma tarefa
    t1.concluir()
    
    print("📋 TODAS AS TAREFAS:")
    print(minha_agenda.listar(apenas_pendentes=False))
    
    print("\n⏳ APENAS PENDENTES:")
    print(minha_agenda.listar(apenas_pendentes=True))
    
    print("\n🔍 BUSCANDO 'MATEMÁTICA':")
    print(minha_agenda.buscar("matemática"))
    
except ValueError as e:
    print(f"Erro de prioridade: {e}")
except LookupError as e:
    print(f"Erro de busca: {e}")