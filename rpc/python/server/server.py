from concurrent import futures
from absl import logging
from absl import app
from absl import flags
from concurrent import futures
from google.protobuf import text_format
from absl import logging
from absl import app
from absl import flags
import grpc
from rpc.proto import service_pb2
from rpc.proto import user_pb2
from rpc.proto import service_pb2_grpc

FLAGS = flags.FLAGS
flags.DEFINE_string('echo', None, 'Text to echo.')


class Server(service_pb2_grpc.RcdServiceServicer):
    def __init__(self, dataPath="rpc/python/data/user.json"):
        with open(dataPath, "rb") as fp:
            # logging.info("data: " + fp.read())
            self.user = user_pb2.User()
            self.user.ParseFromString(fp.read())

    def rec(self, req, context):
        json = text_format.MessageToString(req)
        logging.info("request: " + json)
        return service_pb2.Response()


def serve(argv):
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server = Server()
    logging.info("user: " + str(server.user))

    service_pb2_grpc.add_RcdServiceServicer_to_server(server, grpcServer)
    grpcServer.add_insecure_port('[::]:5300')
    grpcServer.start()
    logging.info("server started......")
    grpcServer.wait_for_termination()


if __name__ == '__main__':
    logging.info("init ok")
    app.run(serve)
