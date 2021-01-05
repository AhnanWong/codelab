package com.codelab.base.protobuf;

import com.codelab.base.file.FileUtils;
import com.google.protobuf.Message;
import com.google.protobuf.TextFormat;

import java.io.File;

/**
 * @ProjectName: codelab
 * @PackageName: base.java.com.codelab.base.protobuf
 * @ClassName: ProtoUtils
 * @Description:
 * @Author: wangyanan
 * @Create: 2021-01-03 12:11
 **/
public class ProtoBufUtils
{
    public static <T extends Message> T file2Proto(String path, Class<T> protoClass) throws TextFormat.ParseException {
        File file = new File(path);
        String content = FileUtils.readString(file);

        return TextFormat.parse(content, protoClass);
    }

    public static <T extends Message> T string2Proto(String string, Class<T> protoClass) throws TextFormat.ParseException {
        return TextFormat.parse(string, protoClass);
    }

}
