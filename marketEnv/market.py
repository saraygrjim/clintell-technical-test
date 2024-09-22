
class Market:
    
    def __init__(self):
        self.currentCardPrice = 200
        self.lastCardPrice    =  self.currentCardPrice
        self.cards            = 100000
        
    def GetCurrentCardPrice(self):
        return self.currentCardPrice
    
    def GetLastCardPrice(self):
        return self.lastCardPrice
    
    def GetStatus(self):
        return self.currentCardPrice, self.cards
    
    def IsSellAllowed(self):
        return True
        
    def Sell(self):
        self.cards = self.cards - 1
        self.currentCardPrice = self.currentCardPrice + (self.currentCardPrice * 0.005)
    
    def Buy(self):
        self.cards = self.cards + 1
        self.currentCardPrice = self.currentCardPrice - (self.currentCardPrice * 0.005)
        
    def CalculateIncrement(self):
        return ((self.currentCardPrice - self.lastCardPrice) / self.lastCardPrice)
    
    def UpdateLastCardPrice(self):
        self.lastCardPrice = self.currentCardPrice
