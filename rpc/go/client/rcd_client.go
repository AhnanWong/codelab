package main

import (
	"codelab.com/rpc/base"
	"codelab.com/rpc/rcd"
	"context"
	"time"

	"google.golang.org/grpc"
)

var log = base.Log
func main() {
	log.Infof("Connect the grpc Server in Go...")
	conn, err := grpc.Dial(":5300", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("fail to dial: %v", err)
	}
	defer conn.Close()
	client := rcd.NewRcdServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
	defer cancel()
	req := &rcd.Request{
		Method: rcd.Method_GET,
		User:   &rcd.User{Id: 1},
		Count:  2,
	}
	str, _ := base.Proto2Json(req)
	log.Infof("request: %s", str)

	rsp, err := client.Rec(ctx, req)
	if err != nil {
		log.Infof("%s.Rec(_) = _, %s: ", client, err)
	}
	str, _ = base.Proto2Json(rsp)
	log.Infof("response: %s", str)
	log.Infof("client done....")
}
