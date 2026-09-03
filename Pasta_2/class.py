class Cachorro:
    #Método construtor
    def __init__(self, nome, raca, tamanho, cor_pelo):
        self.nome = nome
        self.raca = raca
        self.tamanho = tamanho
        self.cor_pelo = cor_pelo
        self.patas = 4

zeca = Cachorro("Zeca", "Viralata", "Médio", "Caramelo")
brutus = Cachorro("Brutus", "Pitbull", "Grande", "Preto")
mel = Cachorro("Mel", "Yorkshire", "Pequeno", "Marrom")

zeca.patas = 3

print(zeca.nome)