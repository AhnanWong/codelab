from abc import ABC, abstractmethod
from Context import Context, User
from Rule import RuleBase

class PostPredictRule(RuleBase):
    @abstractmethod
    def adjust(ctx: Context, user: User):
        print("post predict fill")
        pass


class PostWeightRule(PostPredictRule):
    def __init__(self, wieghtFunc=lambda ctx: True, **kwargs):
        print("post weight init")
        self.wieghtFunc = wieghtFunc
        super(PostWeightRule, self).__init__(**kwargs)

    def adjust(self, ctx: Context, user: User):
        print("post weigth adjust")
