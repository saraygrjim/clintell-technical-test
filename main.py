from market import Market
from agent import Agent, RANDOM_TYPE, TRENDING_TYPE, NON_TRENDING_TYPE, CUSTOM_TYPE, SELL_ACTION, BUY_ACTION
import random
import exceptions as e
  
class Treasurer:
    
    def __init__(self, _days):
        self.days = _days
        self.market = Market()
        nOfTypes = {RANDOM_TYPE: 51, TRENDING_TYPE: 24, NON_TRENDING_TYPE: 24, CUSTOM_TYPE: 1}
        self.agents = list()
        self.agents.extend(Agent(type) for type in nOfTypes.keys() for _ in range(nOfTypes[type]))
    
    def SimulateMarket(self):
        for i in range(self.days):
            print(" DAY " + str(i))
            print("===========")
            self.InitDay()
            
    def InitDay(self):
        orderedAgents = sorted(self.agents, key=lambda y: random.randint(0, len(self.agents)))
        for i in range(0, len(orderedAgents)):
            currentCardPrice = self.market.GetCurrentCardPrice()
            increment = self.market.CalculateIncrement()
            action = orderedAgents[i].SelectAction(currentCardPrice, increment)
            if action == SELL_ACTION:
               self.AgentSell(orderedAgents[i], currentCardPrice)
            
            elif action == BUY_ACTION:
                self.AgentBuy(orderedAgents[i], currentCardPrice)  
                
        # Update market price at the end of the day to consider it the next day
        self.market.UpdateLastCardPrice()
            
    def SimulateMarket(self):
        for i in range(self.days):
            print(" DAY " + str(i))
            print("===========")
            self.InitDay()
        
    def AgentSell(self, agent, currentCardPrice):
        try:
            agent.Sell(currentCardPrice)
        except e.NotEnoughCardsException as exception:
            print(f"Error: {exception}")
        self.market.Buy() 
        
    def AgentBuy(self, agent, currentCardPrice):
        ok = self.market.IsSellAllowed()
        if ok:
            try:
                agent.Buy(currentCardPrice)
            except e.NotEnoughMoneyException as exception:
                print(f"Error: {exception}")
            self.market.Sell() 
        else:
            print(f"Agent {agent.ID} tried to buy, but selling is not allowed.")    
                   
def main():
    t = Treasurer(1000)
    t.SimulateMarket()


if __name__ == "__main__":
    main()

