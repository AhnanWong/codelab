package base

import (
	"bytes"
	"codelab.com/rpc/rcd"
	"github.com/golang/protobuf/jsonpb"
	"github.com/golang/protobuf/proto"
	"go.uber.org/zap"
	"io/ioutil"
	"os"
	"path/filepath"
	"reflect"
	"runtime"
	"strings"
)

var Log *zap.SugaredLogger
func init() {
	logger, _ := zap.NewDevelopment()
	defer logger.Sync()
	Log = logger.Sugar()
}

func TestPath()  {
	_, currentFile, _, _ := runtime.Caller(0)
	basePath := filepath.Dir(currentFile)

	Log.Infof("current file name: ", currentFile)
	Log.Infof("current base path: ", basePath)
	Log.Infof("the files in current path: ")

	var files []string
	filepath.Walk("rpc/", func(path string, info os.FileInfo, err error) error {
		if !info.IsDir() {
			files = append(files, path)
		}
		return nil
	})

	for _, file := range files {
		Log.Infof(file)
	}

	Log.Infof("test path done.")
	Log.Infof("=======================")
}

func LoadData(filePath string) (*rcd.User, error) {
	data, _ := ioutil.ReadFile(filePath)
	user := &rcd.User{}
	Json2Proto(string(data), user)
	str, _ := Proto2Json(user)
	Log.Infof("user pb: ", str)

	Log.Infof("load data done success!!!")

	return user, nil
}

func Proto2Json(p proto.Message) (string, error) {
	m := jsonpb.Marshaler{
		OrigName:     false,
		EnumsAsInts:  true,
		EmitDefaults: false,
		Indent:       "",
		AnyResolver:  nil,
	}
	json, err := m.MarshalToString(p)

	//str, _ := json.Marshal(p)
	return json, err
}

func Json2Proto(str string, p proto.Message) error {
	u := jsonpb.Unmarshaler{
		AllowUnknownFields:true,
		AnyResolver:  nil,
	}
	u.Unmarshal(bytes.NewBuffer([]byte(str)), p)

	//_ = json.Unmarshal([]byte(str), p)
	return nil
}

func GetMessage(pb proto.Message, nameChain string) (proto.Message, error)  {
	names := strings.Split(nameChain, ".")
	sub, _ := GetOrCreate(pb, names[0], false)
	for _, name := range names {
		sub, _ = GetOrCreate(sub, name, false)
		if sub == nil {
			Log.Errorf("name: %s not exist", name)
			return nil, nil
		}
	}
	return sub, nil
}

func GetOrCreate(pb proto.Message, str string, renew bool) (proto.Message, error) {
	rpb := reflect.ValueOf(pb).Elem()
	x := rpb.FieldByName(str)
	if !x.IsValid() {
		Log.Errorf("%s", x)
		return nil, nil
	}
	if !x.IsNil() {
		if  !renew {
			return x.Interface().(proto.Message), nil
		}
	}
	name := proto.MessageName(x.Interface().(proto.Message))
	xx := reflect.New(proto.MessageType(name).Elem())
	xp := reflect.Indirect(xx.Elem()).Addr().Interface().(proto.Message)
	x.Set(reflect.ValueOf(xp))
	return x.Interface().(proto.Message), nil
}
