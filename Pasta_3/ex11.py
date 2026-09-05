class Filme:

    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.assistido = False 

    def marcar_como_assistido(self):
        self.assistido = True


Gente_Grande = Filme("Gente Grande", 120)
Todo_Mundo_Em_Panico = Filme("Todo Mundo em Pânico", 90)

Gente_Grande.marcar_como_assistido()

print(Gente_Grande.assistido)  
print(Todo_Mundo_Em_Panico.assistido)  