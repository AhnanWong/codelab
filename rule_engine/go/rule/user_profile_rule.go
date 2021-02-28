package rule

type UserProfileRule interface {
	RuleBase
	Fill()
}

type BasicUserProfileRule struct {
	UserProfileRule
	WhenFunc func(ctx *Context) bool
}

func (rule *BasicUserProfileRule)Fill()  {
	log.Infof("BasicUserProfileRule fill")
}
func (rule *BasicUserProfileRule)String() string {
	return "BasicUserProfileRule"
}

type RedisUserProfileRule struct {
	UserProfileRule
	WhenFunc func(ctx *Context) bool
}

func (rule *RedisUserProfileRule)Fill()  {
	log.Infof("RedisUserProfileRule fill")
}
