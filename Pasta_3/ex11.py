#a classe Filme representa um filme com título, duração e status de assistido.
class Filme:
    # def = Construtor da classe Filme que inicializa o título, duração e status de assistido.
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.assistido = False 

    # def marcar_como_assistido = Método que marca o filme como assistido, alterando o status para True.
    def marcar_como_assistido(self):
        self.assistido = True

# Exemplo de uso da classe Filme
Gente_Grande = Filme("Gente Grande", 120)
Todo_Mundo_Em_Panico = Filme("Todo Mundo em Pânico", 90)

# Marcar o filme "Gente Grande" como assistido  
Gente_Grande.marcar_como_assistido()

# Verificar o status de assistido dos filmes
print(Gente_Grande.assistido)  
print(Todo_Mundo_Em_Panico.assistido)  