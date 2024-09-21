import uuid
import numpy as np
import exceptions as e

RANDOM_TYPE       = "random"
TRENDING_TYPE     = "trending"
NON_TRENDING_TYPE = "non-trending"
CUSTOM_TYPE       = "custom"
SELL_ACTION       = "sell"
BUY_ACTION        = "buy"
DO_NOTHING_ACTION = "do-nothing"

def select_weighted_action(actions, weights):
    if len(actions) == 1:
        return actions[0]  # If there is only one action, then it is automatically selected
    return np.random.choice(actions, p=weights)
    
class Agent:  
    def __init__(self, _type):
        self.cards  = 0 
        self.ID     = uuid.uuid4()
        self.wallet = 1000
        self.type   = _type
        
        
    def SelectAction(self, currentCardPrice, increment):
        actions = [DO_NOTHING_ACTION]
        action = DO_NOTHING_ACTION
        
        if self.type == RANDOM_TYPE:
            if self.cards > 0: 
                actions.append(SELL_ACTION)
            if self.wallet >= currentCardPrice:
                actions.append(BUY_ACTION) 
            action = np.random.choice(actions) 
        
        elif self.type == TRENDING_TYPE:
            if increment >= 0.01 and self.wallet >= currentCardPrice: 
                actions.append(BUY_ACTION) 
                action = select_weighted_action(actions, [0.25, 0.75]) 
            elif self.cards > 0:
                actions.append(SELL_ACTION)
                action = select_weighted_action(actions, [0.80, 0.20]) 
                
        elif self.type == NON_TRENDING_TYPE:
            if increment <= -0.01 and self.wallet >= currentCardPrice:
                actions.append(BUY_ACTION)
                action = select_weighted_action(actions, [0.25, 0.75])
            elif self.cards > 0: 
                actions.append(SELL_ACTION)
                action = select_weighted_action(actions, [0.80, 0.20])

        elif self.type == CUSTOM_TYPE:
            actions = []
            if self.wallet >= currentCardPrice:
                actions.append(BUY_ACTION)
            if self.cards > 0:
                actions.append(SELL_ACTION)
            action = np.random.choice(actions)
             
        else:
            raise e.InvalidAgentType(f"Invalid agent type: {self.type}")

        
        print(f'Agent {self.ID} has decided the action {action}.')
        return action
    
    def Sell(self, currentCardPrice):
        if self.cards == 0:
            raise e.NotEnoughCardsException(f"Agent {self.id} cannot sell because they have no cards.")
                    
        self.cards = self.cards - 1
        self.wallet = self.wallet + currentCardPrice
        print(f'Agent {self.ID} has sold.')
        self.printCurrentState()
        return
    
    def Buy(self, currentCardPrice):
        if self.wallet < currentCardPrice:
            print("a")
            raise e.NotEnoughMoneyException(f"Agent {self.ID} cannot buy because they do not have enough money.")

        self.cards = self.cards + 1
        self.wallet = self.wallet - currentCardPrice
        print(f'Agent {self.ID} has bought.')
        self.printCurrentState()
        return
        
        
    def printCurrentState(self):
        print(f'Its current state is: Cards={self.cards}, Wallet={self.wallet}.')
    