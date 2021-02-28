from abc import ABC, abstractmethod
from typing import AnyStr, Callable
from Page import Page
from Context import Context, User
from Stage import StageBase, UserProfileStage, CandiStage, CandiFilterStage, PredictStage, PostPredictStage, ResultStage
from UserProfileRule import UserProfileRule, BasicUserProfileRule, RedisUserProfileRule
from CandiRule import CandiRule, EsCandiRule, RedisCandiRule
from CandiFilterRule import CandiFilterRule, SimpleFilterRule
from PredictRule import PredictRule, LRModelRule, DeepModelRule
from PostPredictRule import PostPredictRule, PostWeightRule
from ResultRule import ResultRule, LogRule

class RuleEngine(ABC):
    def __init__(self, *pages):
        check_type = all(isinstance(page, Page) for page in pages)
        if not check_type:
            raise Exception("type error")

        self.pages = pages
        super(RuleEngine, self).__init__()

    def __repr__(self):
        return "%r" % (self.pages)

    def process(self, ctx: Context):
        pagesHit = [page for page in self.pages if page.whenFunc(ctx)]
        for page in pagesHit:
            print('pagehit: ', page)

            user_profile_rules = []
            candi_rules = []
            candi_filter_rules = []
            predict_rules = []
            post_predict_rules = []
            result_rules = []
            for stage in page.stages:
                if isinstance(stage, UserProfileStage):
                    for rule in stage.rules:
                        print('rule: ', rule)
                        user_profile_rules.append(rule)
                elif isinstance(stage, CandiStage):
                    for rule in stage.rules:
                        candi_rules.append(rule)
                elif isinstance(stage, CandiFilterStage):
                    for rule in stage.rules:
                        candi_filter_rules.append(rule)
                elif isinstance(stage, PredictStage):
                    for rule in stage.rules:
                        predict_rules.append(rule)
                elif isinstance(stage, PostPredictStage):
                    for rule in stage.rules:
                        post_predict_rules.append(rule)
                elif isinstance(stage, ResultStage):
                    for rule in stage.rules:
                        result_rules.append(rule)

            for rule in user_profile_rules:
                if rule.whenFunc(ctx):
                    print('rule----', rule)
                    rule.fill(ctx, User())
            for rule in candi_rules:
                rule.candi(ctx, User())
            for rule in candi_filter_rules:
                rule.filter(ctx, User())
            for rule in predict_rules:
                rule.predict(ctx, User())
            for rule in post_predict_rules:
                rule.adjust(ctx, User())
            for rule in result_rules:
                rule.result(ctx, User())



    