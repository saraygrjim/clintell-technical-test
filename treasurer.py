
from market import Market
from agent import Agent, RANDOM_TYPE, TRENDING_TYPE, NON_TRENDING_TYPE, CUSTOM_TYPE, SELL_ACTION, BUY_ACTION
import random
import exceptions as e    
import time
import csv
import os
  
class Treasurer:
    def __init__(self, _days):
        self.days = _days
        self.market = Market()
        nOfTypes = {RANDOM_TYPE: 51, TRENDING_TYPE: 24, NON_TRENDING_TYPE: 24, CUSTOM_TYPE: 1}
        self.agents = list()
        self.agents.extend(Agent(type) for type in nOfTypes.keys() for _ in range(nOfTypes[type]))
        
    def SimulateMarket(self):
        filename = f"market_simulation_{time.time()}.csv" 
        for i in range(self.days):
            self.InitDay()
            writeSummaryToCSV(i, self.agents, self.market, filename)  # daily summary in csv
            if i % 10 == 0:
                print(" DAY " + str(i))
                print("===========")
                summarizeMarket(i, self.agents, self.market)
                time.sleep(0.1)
            
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
  
  
## Functions to show & store sumary data

def summarizeMarket(day, agents, market):
    totalWallet = sum(agent.wallet for agent in agents)
    totalCards = sum(agent.cards for agent in agents)
    
    print(f"Summary for Day {day}:")
    print(f"Total money in market: {totalWallet}")
    print(f"Total cards held by agents: {totalCards}")
    print(f"Current card price: {market.GetCurrentCardPrice()}\n")
    
def writeSummaryToCSV(day, agents, market, filename):
    # verify if file exists
    fileExists = os.path.isfile(filename)
    tmpDir = '.tmp'
    
    if not os.path.exists(tmpDir):
        os.makedirs(tmpDir)
    filePath = os.path.join(tmpDir, filename)
    with open(filePath, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not fileExists:
            # csv headers
            writer.writerow(["Day", "Market Price", "Market Cards Available", 
                             "Agent ID", "Agent Type", "Agent Wallet", "Agent Cards", "Action"])

        # market & agents data
        marketCurrentPrice, marketCards = market.GetStatus()
        for agent in agents:
            id, type, wallet, cards, action = agent.GetStatus()
            writer.writerow([day, marketCurrentPrice, marketCards, id, type, wallet, cards, action])
  