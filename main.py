from market import Market
from agent import Agent, RANDOM_TYPE, TRENDING_TYPE, NON_TRENDING_TYPE, CUSTOM_TYPE, SELL_ACTION, BUY_ACTION, DO_NOTHING_ACTION
import random
  
  
class Treasurer:
    
    def __init__(self, _days):
        self.days = _days
        nOfTypes = {RANDOM_TYPE: 51, TRENDING_TYPE: 24, NON_TRENDING_TYPE: 24, CUSTOM_TYPE: 1}
        # nOfTypes = {RANDOM_TYPE: 2, TRENDING_TYPE: 2, NON_TRENDING_TYPE: 2}

        self.agents = list()
        self.agents.extend(Agent(type) for type in nOfTypes.keys() for _ in range(nOfTypes[type]))
        self.market = Market()
    
    def InitDay(self):
        orderedAgents = sorted(self.agents, key=lambda y: random.randint(0, len(self.agents)))
        for i in range(0, len(self.agents)):
            currentCardPrice = self.market.GetCurrentCardPrice()
            increment = self.market.CalculateIncrement()
            action = orderedAgents[i].SelectAction(currentCardPrice, increment)
            if action == SELL_ACTION:
                orderedAgents[i].Sell(currentCardPrice) #internamente resta 1 a sus tarjetas y suma dinero de currentCardPrice
                self.market.Buy() #suma 1 a sus tarjetas y cambia el precio
            
            elif action == BUY_ACTION:
                ok = self.market.IsSellAllowed() #comprueba que el mercado puede comprar
                if ok:
                    orderedAgents[i].Buy(currentCardPrice) #internamente suma 1 a sus tarjetas y resta dinero de currentCardPrice
                    self.market.Sell() #resta 1 a sus tarjetas y cambia el precio
                if not ok:
                    continue
                    
            else:
                continue
        
        self.market.UpdateLastCardPrice()
            
    def SimulateMarket(self):
        for i in range(self.days):
            print(" DAY " + str(i))
            print("=========== ")
            self.InitDay()
            
    
        
               
def main():
    t = Treasurer(1000)
    t.SimulateMarket()


if __name__ == "__main__":
    main()

