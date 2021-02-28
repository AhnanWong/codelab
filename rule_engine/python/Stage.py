
from typing import Callable
from abc import ABC, abstractmethod
from UserProfileRule import UserProfileRule, BasicUserProfileRule, RedisUserProfileRule
from CandiRule import CandiRule, EsCandiRule, RedisCandiRule
from CandiFilterRule import CandiFilterRule, SimpleFilterRule
from PredictRule import PredictRule, LRModelRule, DeepModelRule
from PostPredictRule import PostPredictRule, PostWeightRule
from ResultRule import ResultRule, LogRule


class StageBase(ABC):
    def __init__(self, id: int, name: str, whenFunc= lambda ctx: True):
        print("stage base init...")
        self.id = id
        self.name = name
        self.whenFunc = whenFunc
        super(StageBase, self).__init__()

class UserProfileStage(StageBase):
    def __init__(self, *rules, whenFunc=lambda ctx: True):
        print("user profile stage init...")

        print('rules=', len(rules))
        print('whenFunc=', whenFunc)
        print('whenFunc callale =', isinstance(whenFunc, Callable))
        print("user profile stage args...")
        for rule in rules:
            print(rule)
        print("===============")

        self.id = 1
        self.name = "user_profile_stage"
        self.whenFunc = whenFunc

        check_type = all(isinstance(rule, UserProfileRule) for rule in rules)
        if not (check_type and isinstance(whenFunc, Callable)):
            raise Exception("type error")
        
        self.rules = rules
        super(UserProfileStage, self).__init__(self.id, self.name, self.whenFunc)

    def __repr__(self):
        return "UserProfileStage(id=%r, name=%r, rule_count=%r)" % (self.id, self.name, len(self.rules))

    def init(self) -> bool:
        for rule in self.rules:
            if not rule.init():
                return False
        return True


class CandiStage(StageBase):
    def __init__(self, *rules, whenFunc=lambda ctx: True):
        print("candi stage init...")
        self.id = 2
        self.name = "candi_stage"
        self.whenFunc = whenFunc

        check_type = all(isinstance(item, CandiRule) for item in rules)
        if not (check_type and isinstance(whenFunc, Callable)):
            raise Exception("type error")
        
        self.rules = rules
        super(CandiStage, self).__init__(self.id, self.name, self.whenFunc)

    def __repr__(self):
        return "CandiStage(id=%r, name=%r, rule_count=%r)" % (self.id, self.name, len(self.rules))

class CandiFilterStage(StageBase):
    def __init__(self, *rules, whenFunc=lambda ctx: True):
        print("candi filter stage init...")
        self.id = 3
        self.name = "candi_filter_stage"
        self.whenFunc = whenFunc

        check_type = all(isinstance(item, CandiFilterRule) for item in rules)
        if not (check_type and isinstance(whenFunc, Callable)):
            raise Exception("type error")

        self.rules = rules
        super(CandiFilterStage, self).__init__(self.id, self.name, self.whenFunc)
        pass

class PredictStage(StageBase):
    def __init__(self, *rules, whenFunc=lambda ctx: True):
        print("predict stage init...")
        self.id = 4
        self.name = "predict_stage"
        self.whenFunc = whenFunc

        check_type = all(isinstance(item, PredictRule) for item in rules)
        if not (check_type and isinstance(whenFunc, Callable)):
            raise Exception("type error")

        self.rules = rules
        super(PredictStage, self).__init__(self.id, self.name, self.whenFunc)
        pass

class PostPredictStage(StageBase):
    def __init__(self, *rules, whenFunc=lambda ctx: True):
        print("post predict stage init...")
        self.id = 5
        self.name = "post_predict_stage"
        self.whenFunc = whenFunc

        check_type = all(isinstance(item, PostPredictRule) for item in rules)
        if not (check_type and isinstance(whenFunc, Callable)):
            raise Exception("type error")

        self.rules = rules
        super(PostPredictStage, self).__init__(self.id, self.name, self.whenFunc)
        pass

class ResultStage(StageBase):
    def __init__(self, *rules, whenFunc=lambda ctx: True):
        print("result stage init...")
        self.id = 6
        self.name = "result_stage"
        self.whenFunc = whenFunc

        check_type = all(isinstance(item, ResultRule) for item in rules)
        if not (check_type and isinstance(whenFunc, Callable)):
            raise Exception("type error")

        self.rules = rules
        super(ResultStage, self).__init__(self.id, self.name, self.whenFunc)
        pass