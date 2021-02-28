package rule

type CandiRule interface {
	RuleBase
	Init()
	Candi()
}

type EsCandiRule struct {
	CandiRule
}

func (rule *EsCandiRule)Candi()  {
	log.Infof("EsCandiRule candi")
}

type RedisCandiRule struct {
	CandiRule
}

func (rule *RedisCandiRule)Candi()  {
	log.Infof("RedisCandiRule candi")
}