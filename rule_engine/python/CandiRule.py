from abc import ABC, abstractmethod
from Context import Context, User
from Rule import RuleBase

class CandiRule(RuleBase):
    @abstractmethod
    def candi(ctx: Context, user: User):
        print("user candi fill")
        pass


class EsCandiRule(CandiRule):
    def __init__(self, index_name="", **kwargs):
        print("es candi init")
        self.index_name = index_name
        super(EsCandiRule, self).__init__(**kwargs)

    def candi(self, ctx: Context, user: User):
        print("es candi fill")


class RedisCandiRule(CandiRule):
    def __init__(self, redis_key="", **kwargs):
        print("redis candi init")
        self.redis_key = redis_key
        super(RedisCandiRule, self).__init__(**kwargs)

    def candi(self, ctx: Context, user: User):
        print("redis candi fill")