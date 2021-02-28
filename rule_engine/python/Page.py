
from typing import Callable
from abc import ABC, abstractmethod
from UserProfileRule import UserProfileRule, BasicUserProfileRule, RedisUserProfileRule
from CandiRule import CandiRule, EsCandiRule, RedisCandiRule
from Stage import StageBase


class Page(ABC):
    def __init__(self, *stages, whenFunc=lambda ctx: True):
        print("page init...")
        self.id = 1
        self.name = "page_stage"
        self.whenFunc = whenFunc

        check_type = all(isinstance(item, StageBase) for item in stages)
        if not (check_type and isinstance(whenFunc, Callable)):
            raise Exception("type error")
        
        self.stages = stages
        super(Page, self).__init__()
        print("page init done...")

    def __repr__(self):
        return "Page(id=%r, name=%r)" % (self.id, self.name)
