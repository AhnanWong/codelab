import grpc
from absl import logging, flags, app
from codelab.grpc.proto import echo_service_pb2
import grpc
from absl import logging, flags, app
from codelab.grpc.proto import echo_service_pb2
from codelab.grpc.proto import echo_service_pb2_grpc

def run(argv):
    # 连接rpc服务器
    channel = grpc.insecure_channel('localhost:50051')
    # # 调用rpc服务
    stub = echo_service_pb2_grpc.EchoServiceStub(channel)
    response = stub.ping(echo_service_pb2.EchoRequest(msg='test'))
    logging.info("client received: " + response.msg)


if __name__ == '__main__':
    app.run(run)