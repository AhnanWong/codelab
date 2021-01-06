from concurrent import futures
from absl import logging
from absl import app
from absl import flags
from concurrent import futures
from absl import logging
from absl import app
from absl import flags
import grpc
from codelab.grpc.proto import echo_service_pb2
from codelab.grpc.proto import echo_service_pb2_grpc


FLAGS = flags.FLAGS
flags.DEFINE_string('echo', None, 'Text to echo.')


class Greeter(echo_service_pb2_grpc.EchoServiceServicer):
    def ping(self, request, context):
        logging.info("request " + request.msg)
        return echo_service_pb2.EchoResponse(msg="ok")


def serve(argv):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_service_pb2_grpc.add_EchoServiceServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("started......")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.info("ok")
    app.run(serve)