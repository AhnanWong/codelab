from abc import ABC, abstractmethod
from Context import Context, User
from Rule import RuleBase

class UserProfileRule(RuleBase):
    @abstractmethod
    def fill(ctx: Context, user: User) -> User:
        print("user profile fill")
        pass


class BasicUserProfileRule(UserProfileRule):
    def __init__(self, **kwargs):
        print("basic profile init")
        super(BasicUserProfileRule, self).__init__(**kwargs)

    def fill(self, ctx: Context, user: User) -> User:
        print("basic profile fill")

class RedisUserProfileRule(UserProfileRule):
    def __init__(self, **kwargs):
        print("redis profile init")
        super(RedisUserProfileRule, self).__init__(**kwargs)

    def fill(self, ctx: Context, user: User) -> User:
        print("redis profile fill")