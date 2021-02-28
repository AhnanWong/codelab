package main

import (
	"codelab.com/rule_engine/go/rule"
)

func main() {
	userProfileRules := make([]rule.UserProfileRule, 0)
	userProfileRules = append(userProfileRules, &rule.BasicUserProfileRule{})
	userProfileRules = append(userProfileRules, &rule.RedisUserProfileRule{})
	userStage := rule.UserProfileStage{
		Rules:     userProfileRules,
		WhenFunc:  nil,
	}
	//fmt.Println(userStage)
	//for _, rule := range userStage.Rules{
	//	rule.Fill()
	//}

	candiRules := make([]rule.CandiRule, 0)
	candiRules = append(candiRules, &rule.EsCandiRule{})
	candiRules = append(candiRules, &rule.RedisCandiRule{})
	candiStage := rule.CandiStage{
		Rules:     candiRules,
		WhenFunc:  nil,
	}
	//fmt.Println(candiStage)
	//for _, rule := range candiStage.Rules{
	//	rule.Candi()
	//}

	stages := make([]rule.StageBase, 0)
	stages = append(stages, userStage)
	stages = append(stages, candiStage)
	page := &rule.Page{
		Stages:   stages,
		WhenFunc: nil,
	}

	engine := rule.RuleEngine{
		Pages: []rule.Page{*page},
	}

	engine.Process(&rule.Context{})
}
