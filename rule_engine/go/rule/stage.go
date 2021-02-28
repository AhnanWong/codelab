package rule

type StageBase interface {
}

type UserProfileStage struct {
	StageBase
	Rules []UserProfileRule
	WhenFunc func(ctx *Context) bool
}

type CandiStage struct {
	StageBase
	Rules []CandiRule
	WhenFunc func(ctx *Context) bool
}

type PredictStage struct {
	StageBase
	Rules []PredictRule
	WhenFuc func(ctx *Context) bool
}

type PostPredictWeightStage struct {
	StageBase
	Rules []PostPredictRule
	WhenFuc func(ctx *Context) bool
}

type ResultStage struct {
	StageBase
	Rules []ResultRule
	WhenFuc func(ctx *Context) bool
}
