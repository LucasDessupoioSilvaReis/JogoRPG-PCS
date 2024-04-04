class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.sabedoria = 0
        self.inteligencia = 0
        self.carisma = 0

    def distribuir_pontos(self):
        pontos_disponiveis = 20
        atributos = ['forca', 'destreza', 'constituicao', 'sabedoria', 'inteligencia', 'carisma']
        while pontos_disponiveis > 0:
            print(f"\nVoce tem {pontos_disponiveis} pontos disponiveis para distribuir.")
            print("Atributos disponíveis:")
            for i, atributo in enumerate(atributos):
                print(f"{i + 1}. {atributo.capitalize()}")
            escolha = input("Escolha o atributo (pelo Nome) que deseja aumentar (ou digite 'sair' para finalizar): ").lower()
            if escolha == 'sair':
                break
            elif escolha in atributos:
                pontos = int(input("Quantos pontos vc quer adicionar nesse atributo? "))
                if pontos_disponiveis >= pontos:
                    setattr(self, escolha, getattr(self, escolha) + pontos)
                    pontos_disponiveis -= pontos
                else:
                    print("Você não tem tantos pontos!")
            else:
                print("Escolha não existente!")

    def info(self):
        return f"Nome: {self.nome}\nClasse: {self.classe}\nForça: {self.forca}\nDestreza: {self.destreza}\nConstituição: {self.constituicao}\nSabedoria: {self.sabedoria}\nInteligência: {self.inteligencia}\nCarisma: {self.carisma}"
