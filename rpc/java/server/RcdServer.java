package rpc.java.server;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * @author wangyanan
 */
public class RcdServer
{
    private Server server;
    private static final Logger log = LogManager.getLogger(RcdServer.class);
    public RcdServer(int port) {
        RcdServerImpl serverImpl = new RcdServerImpl();
        serverImpl.init("rpc/java/data/user.json");

        server = ServerBuilder.forPort(port)
                .addService(serverImpl)
                .build();
    }

    public void start() throws IOException
    {
        try {
            server.start();
            server.awaitTermination();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void awaitTermination()
    {
        try {
            server.awaitTermination();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void shutdown() {
        server.shutdown();
    }

    public static void main(String[] args) throws IOException {
        log.info("server start...");

        RcdServer server = new RcdServer(5300);
        server.start();
        log.info("job done!!!");
    }
}