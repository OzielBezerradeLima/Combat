class Tank:

    def __init__(self, player, x, y, direction):
        self.player = player
        self.bombs = []
        self.x = x
        self.y = y
        self.direction = direction

    def movement(self, key):
        match key:
            case "W":
                match self.direction:
                    case 0:
                        self.y += 1
                    case 45:
                        self.x += 1
                        self.y += 1
                    case 90:
                        self.x += 1
                    case 135:
                        self.x += 1
                        self.y -= 1
                    case 180:
                        self.y -= 1
                    case 225:
                        self.x -= 1
                        self.y -= 1
                    case 270:
                        self.x -= 1
                    case 315:
                        self.x -= 1
                        self.y += 1

                print(self.player, "moveu-se pra frente com sucesso para [", self.x, ",", self.y, "]")
            case "A":
                self.direction -= 45
                if abs(self.direction) == 0:
                    self.direction = 315
                print(self.player, "girou para a esquerda com sucesso")
            case "D":
                self.direction += 45
                if abs(self.direction) == 360:
                    self.direction = 0
                print(self.player, "girou para a direita com sucesso")
            case "S":
                new_bomb = {'player': self.player, 'x': self.x, 'y': self.y,
                            'direction': self.direction, 'life_span': 5}
                self.bombs.append(new_bomb)
                print(self.player, "atirou com sucesso")

    def move_bombs(self):
        for bomb in self.bombs:
            while bomb['life_span'] > 0:
                match bomb['direction']:
                    case 0:
                        bomb['x'] += 1
                    case 45:
                        bomb['x'] += 1
                        bomb['y'] += 1
                    case 90:
                        bomb['x'] += 1
                    case 135:
                        bomb['x'] += 1
                        bomb['y'] -= 1
                    case 180:
                        bomb['y'] -= 1
                    case 225:
                        bomb['x'] -= 1
                        bomb['y'] -= 1
                    case 270:
                        bomb['x'] -= 1
                    case 315:
                        bomb['x'] -= 1
                        bomb['y'] += 1
                bomb['life_span'] -= 1
                print("Posição da bomba atirada pelo ", bomb['player'], " [", bomb['x'], ", ", bomb['y'], "]")
            self.bombs.remove(bomb)
