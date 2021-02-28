package rule

type PostPredictRule interface {
	RuleBase
	Init()
	Weight()
}

type SimpleWeightRule struct {
	PostPredictRule
}

func (rule *SimpleWeightRule)Weight()  {
	log.Infof("SimpleWeightRule fill")
}
