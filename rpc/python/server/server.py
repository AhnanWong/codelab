from concurrent import futures
from absl import logging
from absl import app
from absl import flags
from concurrent import futures
from google.protobuf.json_format import Parse
from google.protobuf import text_format
from google.protobuf import json_format
from absl import logging
from absl import app
from absl import flags
import grpc
from rpc.proto import service_pb2
from rpc.proto import user_pb2, item_pb2, common_pb2
from rpc.proto import service_pb2_grpc

FLAGS = flags.FLAGS
flags.DEFINE_string('echo', None, 'Text to echo.')


class Server(service_pb2_grpc.RcdServiceServicer):
    def __init__(self, dataPath="rpc/python/data/user.json"):
        with open(dataPath, "r") as fp:
            self.user = Parse(fp.read(), user_pb2.User(), ignore_unknown_fields=True)
            js = json_format.MessageToJson(self.user, including_default_value_fields=True)
            logging.info("my user: " + js)
        logging.info("load data success....")

    def rec(self, req, context):
        json = json_format.MessageToJson(req)
        logging.info("context: " + str(context))
        logging.info("request: " + json)

        user = self.user
        if req.user.id != user.id:
            return service_pb2.Response(result=common_pb2.Result(code=-1, message="can not find the user."),
                                        context=service_pb2.Context(user=req.user))

        rsp = service_pb2.Response(result=common_pb2.Result(code=0, message="find the user."))
        count = req.count
        actions = [a for a in user.action]
        actions.sort(key=lambda x: x.score, reverse=True)

        items = [a.item for a in actions[:count]]

        ctx = service_pb2.Context(user=user)
        ctx.item_list.extend(items)
        rsp.context.MergeFrom(ctx)

        json = json_format.MessageToJson(rsp)
        logging.info("response: " + json)
        return rsp


def serve(argv):
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server = Server()

    service_pb2_grpc.add_RcdServiceServicer_to_server(server, grpcServer)
    grpcServer.add_insecure_port('[::]:5300')
    grpcServer.start()
    logging.info("server started......")
    grpcServer.wait_for_termination()


if __name__ == '__main__':
    logging.info("init ok")
    app.run(serve)
