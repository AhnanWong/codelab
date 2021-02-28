package rule

type RuleEngine struct {
	Pages []Page
}

func (engine *RuleEngine)Init(page Page)  {

}

func (engine *RuleEngine)Process(ctx *Context)  {
	userProfileRules := make([]UserProfileRule, 0)
	candiRules := make([]CandiRule, 0)
	predictRules := make([]PredictRule, 0)
	postPredictRules := make([]PostPredictRule, 0)
	resultRules := make([]ResultRule, 0)

	var page Page
	for _, p := range engine.Pages {
		p.Init()
		if p.WhenFunc(ctx) {
			page = p
		}
	}

	for _, stage := range page.Stages {
		if profileStage, ok := stage.(UserProfileStage); ok {
			for _, rule := range profileStage.Rules {
				userProfileRules = append(userProfileRules, rule)
			}
		}

		if candiStage, ok := stage.(CandiStage); ok {
			for _, rule := range candiStage.Rules {
				candiRules = append(candiRules, rule)
			}
		}

		if predictStage, ok := stage.(PredictStage); ok {
			for _, rule := range predictStage.Rules {
				predictRules = append(predictRules, rule)
			}
		}

		if postPredictStage, ok := stage.(PostPredictWeightStage); ok {
			for _, rule := range postPredictStage.Rules {
				postPredictRules = append(postPredictRules, rule)
			}
		}

		if ResultStage, ok := stage.(ResultStage); ok {
			for _, rule := range ResultStage.Rules {
				resultRules = append(resultRules, rule)
			}
		}
	}

	for _, rule := range userProfileRules {
		rule.Fill()
	}

	for _, rule := range candiRules {
		rule.Candi()
	}

	for _, rule := range predictRules {
		rule.Predict()
	}

	for _, rule := range postPredictRules {
		rule.Weight()
	}

	for _, rule := range resultRules {
		rule.Result()
	}
}
