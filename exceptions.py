class AgentException(Exception):
    pass

class NotEnoughCardsException(AgentException):
    pass

class NotEnoughMoneyException(AgentException):
    pass

class InvalidAgentType(AgentException):
    pass