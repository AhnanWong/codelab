package com.codelab.base.file;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * @ProjectName: codelab
 * @PackageName: base.java.com.codelab.base
 * @ClassName: Files
 * @Description:
 * @Author: wangyanan
 * @Create: 2021-01-03 12:09
 **/
public class FileUtils
{
    public static String readString(String fileName) {
        return readString(new File(fileName));
    }

    public static String readString(File file) {
        String content = null;
        if (!file.exists()) {
            return null;
        }

        byte[] bytes;
        try {
            bytes = Files.readAllBytes(Paths.get(file.getPath()));
            content = new String(bytes);
        } catch (IOException e) {
            e.printStackTrace();
        }

        return content;
    }
}
