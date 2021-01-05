package rpc.java.client;

import com.codelab.rpc.rcd.Common;
import com.codelab.rpc.rcd.UserOuterClass;
import com.google.protobuf.util.JsonFormat;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import com.codelab.rpc.rcd.Service;
import com.codelab.rpc.rcd.RcdServiceGrpc;

/**
 * @author wangyanan
 */
public class RcdClient
{
    private final RcdServiceGrpc.RcdServiceBlockingStub stub;
    public RcdClient(String host, int port) {
        ManagedChannel channel = ManagedChannelBuilder.forAddress(host, port)
                .usePlaintext()
                .build();

        stub = RcdServiceGrpc.newBlockingStub(channel);
    }

    public String rec(int uid, int count) {
        Service.Request req = Service.Request.newBuilder()
                .setMethod(Common.Method.GET)
                .setUser(UserOuterClass.User.newBuilder().setId(uid))
                .setCount(count)
                .build();
        Service.Response rsp = stub.rec(req);

        String json = "";
        try {
            json = JsonFormat.printer().print(rsp);
            System.out.println("收到的数据: ");
            System.out.println(json);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return json;
    }


    public static void main(String[] args) {
        System.out.println("job start...");
        RcdClient client = new RcdClient("localhost", 5100);
        String rsp = client.rec(1, 2);
        System.out.println("job done!!!");
    }
}