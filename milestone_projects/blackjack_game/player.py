from card import Card

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.points = 0
        self.aces = 0

    def __str__(self) -> str:
        return f'My name is {self.name}'   

    def adjustPointsOfAces(self):
        while self.points > 21 and self.aces:
            self.points -= 10
            self.aces -= 1

    def addPoints(self, newCard):
        self.points += newCard.face_value

        if newCard.rank == 'Ace':
            self.aces += 1
            
        self.adjustPointsOfAces()