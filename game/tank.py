from bomb import Bomb


class Tank:

    def __init__(self, player):
        self.player = player
        self.bombs = []

    def movement(self, key):
        match key:
            case "W":
                print(self.player, "moveu-se pra frente com sucesso")
            case "A":
                print(self.player, "girou para a esquerda com sucesso")
            case "D":
                print(self.player, "girou para a direita com sucesso")
            case "S":
                self.bombs.append()
                print(self.player, "atirou com sucesso")
