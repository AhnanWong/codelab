package rule

type ResultRule interface {
	RuleBase
	Init()
	Result()
}

type ResultLogRule struct {
	ResultRule
}

func (rule *ResultLogRule)Result()  {
	log.Infof("ResultLogRule fill")
}
