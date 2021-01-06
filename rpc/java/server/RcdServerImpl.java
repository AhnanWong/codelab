package rpc.java.server;

import com.codelab.base.file.FileUtils;
import com.codelab.rpc.rcd.*;
import com.google.protobuf.util.JsonFormat;
import io.grpc.stub.StreamObserver;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.LinkedList;
import java.util.List;

/**
 * @author wangyanan
 */
public class RcdServerImpl extends RcdServiceGrpc.RcdServiceImplBase
{
    UserOuterClass.User.Builder user;
    private static final Logger log = LogManager.getLogger(RcdServer.class);
    public void RcdServerImpl() {
    }

    public void init(String filePath) {
        String content = FileUtils.readString(filePath);
        UserOuterClass.User.Builder builder = UserOuterClass.User.newBuilder();
        try {
            log.info(content);
            JsonFormat.parser().merge(content, builder);
            String json = JsonFormat.printer().print(builder);
            log.info(json);
            log.info("read json done!");
        } catch (Exception e) {
            e.printStackTrace();
        }

        this.user = builder;
    }

    public void initContext(Service.Response.Builder rsp, Service.Request req) {
        UserOuterClass.User.Builder user = this.user;
        Service.Context.Builder ctx = Service.Context.newBuilder();
        int uid = req.getUser().getId();
        if (uid != user.getId()) {
            ctx.setUser(req.getUser());
            rsp.setContext(ctx).setResult(
                    Common.Result.newBuilder().setCode(-1)
                    .setMessage("can not find the user.")
            );
            return;
        }

        user.mergeFrom(req.getUser());
        int count = req.getCount();
        List<UserOuterClass.Action> actions = new LinkedList<>(user.getActionList());
        actions.sort((o1, o2) -> Float.compare(o2.getScore(), o1.getScore()));

        ctx.setUser(user);
        List<ItemOuterClass.Item> items = new LinkedList<>();
        int i = 0;
        for (UserOuterClass.Action action: actions) {
            if (++i > count) {
                break;
            }
            items.add(action.getItem());
        }
        ctx.addAllItemList(items);

        rsp.setContext(ctx).setResult(
                Common.Result.newBuilder().setCode(0)
                        .setMessage("success find the user.")
        );
    }

    public void process(Service.Response.Builder rsp) {
        DateFormat df = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = new Date();
        String time = df.format(date);
        rsp.setTime(time);
    }

    @Override
    public void rec(Service.Request req, StreamObserver<Service.Response> responseObserver) {
        Service.Response.Builder rsp = Service.Response.newBuilder();
        initContext(rsp, req);
        process(rsp);

        try {
            String json = JsonFormat.printer().print(req);
            log.info("收到数据: ");
            log.info(json);

            json = JsonFormat.printer().print(rsp);
            log.info("返回数据: ");
            log.info(json);
        } catch (Exception e) {
            e.printStackTrace();
        }

        responseObserver.onNext(rsp.build());
        responseObserver.onCompleted();
    }
}