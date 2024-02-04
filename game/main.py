from tank import Tank

still_playing = True
a = Tank("Player 1", 0, 0, 0)

print("Comandos:\nW - Mover pra Frente\nA - Girar pra Esquerda"
      "\nD - Girar pra Direita\nS - Atirar\nX - Parar de Jogar")

while still_playing:
    option = input("Escolha a sua ação: ")
    if option == "X":
        still_playing = False
    else:
        Tank.movement(a, option)
    Tank.move_bombs(a)
    