package http.java;

import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;

/**
 * @author admin
 */
public class HelloServer
{
    public static void main(String[] args) throws IOException
    {
        HttpServer httpServer = HttpServer.create(new InetSocketAddress(9090), 0);
        httpServer.createContext("/hello", new MyHandler());
        httpServer.start();
        System.out.println("server start...");
    }

}
