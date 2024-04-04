from personagem import Personagem

if __name__ == "__main__":
    print("Boas vindas ao jogo de RPG(Não terminado)!\n")

    nome = input("Qual seria seu nome de Invocador: ")

    print("\nEscolha uma classe dentre as 15:")
    print("1. Dwarf")
    print("2. Hill Dwarf")
    print("3. Ladino")
    print("4. Dwarf")
    print("5. Hill Dwarf")
    print("6. Ladino")
    print("7. Dwarf")
    print("8. Hill Dwarf")
    print("9. Ladino")
    print("10. Dwarf")
    print("11. Hill Dwarf")
    print("12. Ladino")
    print("13. Dwarf")
    print("14. Hill Dwarf")
    print("15. Ladino")
    classe_escolhida = int(input("Escolha a classe digitando seu numero! : "))

    if classe_escolhida == 1:
        classe = "Dwarf"
    elif classe_escolhida == 2:
        classe = "Hill Dwarf"
    elif classe_escolhida == 3:
        classe = "Mountain Dwarf"
    elif classe_escolhida == 4:
        classe = "Elf"
    elif classe_escolhida == 5:
        classe = "High Elf"
    elif classe_escolhida == 6:
        classe = "Wood Elf"
    elif classe_escolhida == 7:
        classe = "Dark Elf Drow"
    elif classe_escolhida == 8:
        classe = "Barbaro"
    elif classe_escolhida == 9:
        classe = "Lightfoot"
    elif classe_escolhida == 10:
        classe = "Human"
    elif classe_escolhida == 11:
        classe = "Dragonborn"
    elif classe_escolhida == 12:
        classe = "Gnome"
    elif classe_escolhida == 13:
        classe = "Forest Gnome"
    elif classe_escolhida == 14:
        classe = "Rock Gnome"
    elif classe_escolhida == 15:
        classe = "Tiefling"
    else:
        print("Escolha negada, Escolha entre 1 e 15.")
        exit()

    jogador = Personagem(nome, classe)
    jogador.distribuir_pontos()

    print("\nAtributo de seu personagem:")
    print(jogador.info())
