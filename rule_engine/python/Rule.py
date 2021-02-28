
from abc import ABC, abstractmethod
from typing import AnyStr, Callable

class RuleBase(ABC):
    def __init__(self, id: int, name: str, whenFunc= lambda ctx: True):
        print("rule base init...")
        self.id = id
        self.name = name
        self.whenFunc = whenFunc
        super(RuleBase, self).__init__()

    def __repr__(self):
        return "Rule(id=%r, name=%r, whenFunc=%r)" % (self.id, self.name, self.whenFunc)