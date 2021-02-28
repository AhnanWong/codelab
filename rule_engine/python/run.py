from typing import AnyStr, Callable
from Rule import RuleBase
from Context import Context, User
from RuleEngine import RuleEngine
from Page import Page
from Stage import StageBase, UserProfileStage, CandiStage, CandiFilterStage, PredictStage, PostPredictStage, ResultStage
from UserProfileRule import UserProfileRule, BasicUserProfileRule, RedisUserProfileRule
from CandiRule import CandiRule, EsCandiRule, RedisCandiRule
from CandiFilterRule import CandiFilterRule, SimpleFilterRule
from PredictRule import PredictRule, LRModelRule, DeepModelRule
from PostPredictRule import PostPredictRule, PostWeightRule
from ResultRule import ResultRule, LogRule


# rule1 = BasicUserProfileRule(id=0, name='basic user rule', whenFunc=lambda x, y: x+y)
# print(rule1.name)


# rule2 = RedisUserProfileRule(id=0, name='redis user rule', whenFunc=lambda x, y: x+y)
# print(rule2.name)

# print(isinstance(rule2, BasicUserProfileRule))
# print(isinstance(rule2, UserProfileRule))
# print(isinstance(rule2, RuleBase))
# print(isinstance(rule2, RedisUserProfileRule))
# print(isinstance(rule2, UserProfileStage))


# a = UserProfileStage(
#     BasicUserProfileRule(id=0, name='basic user rule', whenFunc=lambda x, y: x+y), 
#     RedisUserProfileRule(id=0, name='redis user rule', whenFunc=lambda x, y: x+y)
# )
# print(a)
# for rule in a.rules:
#     rule.fill(ctx=Context(), user=User())

# b = CandiStage(
#     EsCandiRule(id=0, name='basic user rule', whenFunc=lambda x, y: x+y), 
#     RedisCandiRule(id=0, name='redis user rule', whenFunc=lambda x, y: x+y)
# )
# print(b)
# for rule in b.rules:
#     rule.candi(ctx=Context(), user=User())

page = Page(
    UserProfileStage(
        BasicUserProfileRule(id=0, name='basic user rule'), 
        RedisUserProfileRule(id=1, name='redis user rule', whenFunc=lambda ctx: False), 
        whenFunc = lambda ctx: True
    ), 
    CandiStage(
        EsCandiRule(id=0, name='es candi rule', index_name="es_index_test", whenFunc=lambda ctx: True), 
        RedisCandiRule(id=1, name='redis candi rule_1', redis_key="redis_test_1", whenFunc=lambda ctx: True), 
        RedisCandiRule(id=2, name='redis candi rule_2', redis_key="redis_test_2", whenFunc=lambda ctx: True)
    ), 
    CandiFilterStage(
        SimpleFilterRule(id=0, name='simple filter rule', filterFunc=lambda ctx: True, whenFunc=lambda ctx: True)
    ), 
    PredictStage(
        LRModelRule(id=0, name='lr model rule', whenFunc=lambda ctx: True)
    ), 
    PostPredictStage(
        PostWeightRule(id=0, name='post weight rule', wieghtFunc=lambda ctx: True, whenFunc=lambda ctx: True), 
    ), 
    ResultStage(
        LogRule(id=0, name='result rule', whenFunc=lambda ctx: True), 
    ), 
    whenFunc = lambda ctx: True
)

# print(page.stages[1])
for stage in page.stages:
    print('stage=', stage)
    for rule in stage.rules:
        print('rule=', rule)
        # print('id: ', rule.id)
        # print('name: ', rule.name)

engine = RuleEngine(page)
print("rule engine.......")
engine.process(Context())
    
# print('testadfjlaksflajfla', p1.stages[1].rules[0].index_name)
# x=lambda x, y: x+y
# print('', isinstance(x, Callable))
