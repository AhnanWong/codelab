package rule

type PredictRule interface {
	RuleBase
	Init()
	Predict()
}

type PredictModelRule struct {
	PredictRule
}

func (rule *PredictModelRule)Predict()  {
	log.Infof("PredictModelRule fill")
}