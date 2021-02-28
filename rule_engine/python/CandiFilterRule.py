from abc import ABC, abstractmethod
from Context import Context, User
from Rule import RuleBase

class CandiFilterRule(RuleBase):
    @abstractmethod
    def filter(ctx: Context, user: User):
        print("user candi fill")
        pass


class SimpleFilterRule(CandiFilterRule):
    def __init__(self, filterFunc=lambda ctx: True, **kwargs):
        print("es candi init")
        self.filterFunc = filterFunc
        super(SimpleFilterRule, self).__init__(**kwargs)

    def filter(self, ctx: Context, user: User):
        print("es candi fill")
