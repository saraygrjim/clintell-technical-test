import uuid
import numpy as np

RANDOM_TYPE       = "random"
TRENDING_TYPE     = "trending"
NON_TRENDING_TYPE = "non-trending"
CUSTOM_TYPE       = "custom"
SELL_ACTION       = "sell"
BUY_ACTION        = "buy"
DO_NOTHING_ACTION = "do-nothing"

class Agent:  
    def __init__(self, _type):
        self.cards  = 0 
        self.id     = uuid.uuid4()
        self.wallet = 1000
        self.type   = _type
        
    def SelectAction(self, currentCardPrice, increment):
        action = DO_NOTHING_ACTION
        actions = [DO_NOTHING_ACTION]
        if self.type == RANDOM_TYPE:
            if self.cards > 0: # if the agent has no cards then sell action is not allowed
                actions.append(SELL_ACTION)
            if self.wallet >= currentCardPrice: # if the agent has no enought money then buy action is not allowed
                actions.append(BUY_ACTION) 
            action = np.random.choice(actions) 
        
        elif self.type == TRENDING_TYPE:
            if increment >= 0.01 and self.wallet >= currentCardPrice: # if the agent has no enought money then buy action is not allowed
                actions.append(BUY_ACTION) 
                weigths = [0.25, 0.75]
                action = np.random.choice(actions, p=weigths)   
            else:
                if self.cards > 0: # if the agent has no cards then sell action is not allowed
                    actions.append(SELL_ACTION) 
                    weigths = [0.80, 0.20]
                    action = np.random.choice(actions, p=weigths)   
                
        elif self.type == NON_TRENDING_TYPE:
            if increment <= -0.01:
                if self.wallet >= currentCardPrice: # if the agent has no enought money then buy action is not allowed
                    actions.append(BUY_ACTION) 
                    weigths = [0.25, 0.75]
                    action = np.random.choice(actions, p=weigths)   
            else:
                if self.cards > 0: # if the agent has no cards then sell action is not allowed
                    actions.append(SELL_ACTION) 
                    weigths = [0.80, 0.20]
                    action = np.random.choice(actions, p=weigths)  
                
        elif self.type == CUSTOM_TYPE:
            actions = []
            if self.wallet >= currentCardPrice:
                actions.append(BUY_ACTION) 
            if self.cards > 0:
                actions.append(SELL_ACTION) 
            action = np.random.choice(actions)  
        
        else:
            return "invalid type"     
        
        print(f'Agent {self.id} has decided the action {action}.')
        return action
    
    def Sell(self, currentCardPrice):
        # if self.cards == 0:
        #    return error
        self.cards = self.cards - 1
        self.wallet = self.wallet + currentCardPrice
        print(f'Agent {self.id} has sold.')
        self.printCurrentState()
        return
    
    def Buy(self, currentCardPrice):
        # if self.wallet < currentCardPrice:
        #    return error
        self.cards = self.cards + 1
        self.wallet = self.wallet - currentCardPrice
        print(f'Agent {self.id} has bought.')
        self.printCurrentState()
        return
        
        
    def printCurrentState(self):
        print(f'Its current state is: Cards={self.cards}, Wallet={self.wallet}.')
    
    