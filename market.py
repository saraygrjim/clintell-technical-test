
class Market:
    
    def __init__(self):
        self.currentCardPrice = 200
        self.lastCardPrice    =  self.currentCardPrice
        self.cards            = 100000
        
    def GetCurrentCardPrice(self):
        return self.currentCardPrice
    
    def GetLastCardPrice(self):
        return self.lastCardPrice
    
    def IsSellAllowed(self):
        # return self.cards > 0
        return True
        
    def Sell(self):
        self.cards = self.cards - 1
        self.currentCardPrice = self.currentCardPrice + (self.currentCardPrice * 0.005)
        self.printCurrentState()
    
    def Buy(self):
        self.cards = self.cards + 1
        self.currentCardPrice = self.currentCardPrice - (self.currentCardPrice * 0.005)
        self.printCurrentState()
        
    def CalculateIncrement(self):
        return ((self.currentCardPrice - self.lastCardPrice) / self.lastCardPrice)
    
    
    def UpdateLastCardPrice(self):
        self.lastCardPrice = self.currentCardPrice
        
    def printCurrentState(self):
        print(f'Market current state is: Cards={self.cards}, CurrentCardPrice={self.currentCardPrice}.')
    
    