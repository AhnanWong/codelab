package rule

type Page struct {
	Stages []StageBase
	WhenFunc func(ctx *Context) bool
}

func (p *Page)Init()  {
	p.WhenFunc = func(ctx *Context) bool {
		return true
	}
}