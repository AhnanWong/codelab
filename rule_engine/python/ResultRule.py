from abc import ABC, abstractmethod
from Context import Context, User
from Rule import RuleBase

class ResultRule(RuleBase):
    @abstractmethod
    def result(ctx: Context, user: User):
        print("user candi fill")
        pass


class LogRule(ResultRule):
    def __init__(self, **kwargs):
        print("es candi init")
        super(LogRule, self).__init__(**kwargs)

    def result(self, ctx: Context, user: User):
        print("es candi fill")
