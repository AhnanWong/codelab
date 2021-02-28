from abc import ABC, abstractmethod
from Context import Context, User
from Rule import RuleBase

class PredictRule(RuleBase):
    @abstractmethod
    def predict(ctx: Context, user: User):
        print("user candi fill")
        pass


class LRModelRule(PredictRule):
    def __init__(self, **kwargs):
        print("lr model init")
        super(LRModelRule, self).__init__(**kwargs)

    def predict(self, ctx: Context, user: User):
        print("lr model predict")


class DeepModelRule(PredictRule):
    def __init__(self, **kwargs):
        print("deep model init")
        super(DeepModelRule, self).__init__(**kwargs)

    def predict(self, ctx: Context, user: User):
        print("deep model predict")