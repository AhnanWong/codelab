package main

import (
	"codelab.com/rpc/base"
	"codelab.com/rpc/rcd"
	"flag"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"net"
	"sort"
)

type RcdServer struct {
	user    *rcd.User
	context *rcd.Context
}

func (cs *RcdServer) Rec(ctx context.Context, req *rcd.Request) (*rcd.Response, error) {
	log.Infof("context: %s", ctx)
	log.Infof("method: %s", req.GetMethod())
	str, _ := base.Proto2Json(req)
	log.Infof("request: %s", str)

	user := req.User
	count := req.Count
	rsp := &rcd.Response{
		Result:  &rcd.Result{Code: -1, Message: "can not find the user."},
		Context: &rcd.Context{User: user, ItemList: nil},
	}

	if cs.user.Id != user.Id {
		return rsp, nil
	}

	rsp.Result = &rcd.Result{Code:0, Message:"success get the user."}
	actions := cs.user.GetAction()
	sort.SliceStable(actions, func(i, j int) bool {
		return actions[i].Score > actions[j].Score
	})

	items := make([]*rcd.Item, 0)
	for idx, action := range actions {
		if idx < int(count) {
			items = append(items, action.Item)
		}
	}
	rsp.Context = &rcd.Context{
		User: cs.user,
		ItemList: items,
	}

	str, _ = base.Proto2Json(rsp)
	log.Infof("response: %s", str)

	return rsp, nil
}

var dataPath = flag.String("path", "rpc/go/data/user.json", "user data json")
var log = base.Log

func main() {
	flag.Parse()

	log.Infof("data path: %s", *dataPath)
	base.TestPath()

	user, _ := base.LoadData(*dataPath)

	listen, err := net.Listen("tcp", ":5300")
	if err != nil {
		log.Infof("Unable to listen: ", err.Error())
	}
	defer listen.Close()
	defer log.Infof("Connection closed.")

	grpcServer := grpc.NewServer()
	server := &RcdServer{
		user: user,
	}
	rcd.RegisterRcdServiceServer(grpcServer, server)

	log.Infof("listening...")
	err = grpcServer.Serve(listen)
	if err != nil {
		log.Errorf("Unable to start serving! Error: " + err.Error())
	}
}
