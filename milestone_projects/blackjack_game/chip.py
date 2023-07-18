class Chip:
    def __init__(self, total = 100) -> None:
        self.total = total
        self.bet = 0
    
    def winBet(self):
        self.total += self.bet
    
    def loseBet(self):
        self.total -= self.bet