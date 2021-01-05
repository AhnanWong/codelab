import grpc
from absl import logging, flags, app
import grpc
from absl import logging, flags, app
from rpc.proto import service_pb2
from rpc.proto import common_pb2
from rpc.proto import user_pb2
from rpc.proto import service_pb2_grpc
from google.protobuf import text_format


def run(argv):
    channel = grpc.insecure_channel('localhost:5300')
    stub = service_pb2_grpc.RcdServiceStub(channel)
    user = user_pb2.User(id=1)
    rsp = stub.rec(service_pb2.Request(method=common_pb2.GET, user=user, count=2))
    json = text_format.MessageToString(rsp)
    logging.info("client received: " + json)


if __name__ == '__main__':
    app.run(run)
