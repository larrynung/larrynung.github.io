---
title: "ghz - Benchmark with template data"
date: "2019-07-10 07:15:11"
tags: [ghz]
---


在用 ghz 做 gRPC 的 Benchmark 時，如果需要打入不同的測試資料，又不想要撰寫程式的話，可使用 ghz 的 Template data。  

<!-- More -->

</br>


ghz 提供的 Template data 如下:  

```
// call template data
type callTemplateData struct {

    // unique worker ID
    WorkerID           string

    // unique incremented request number for each request
    RequestNumber      int64

    // fully-qualified name of the method call
    FullyQualifiedName string

    // shorter call method name
    MethodName         string

    // the service name
    ServiceName        string

    // name of the input message type
    InputName          string

    // name of the output message type
    OutputName         string

    // whether this call is client streaming
    IsClientStreaming  bool

    // whether this call is server streaming
    IsServerStreaming  bool

    // timestamp of the call in RFC3339 format
    Timestamp          string

    // timestamp of the call as unix time
    TimestampUnix      int64
}
```

</br>


裡面有 Worker 編號、Request 編號、Method 名稱、Service 名稱、傳入的 Message 名稱、傳出的 Message 名稱、是否 Streaming、RFC3339 格式的時間、Unix 時間。  

</br>


可視需要帶入 ghz 的 Data 或是 MetaData，Benchmark 時 ghz 會自動帶入對應的值。  

</br>


像是如果要用 Template data 設定 MetaData 的 request-id 與 timestamp，可以像下面這樣帶入 ghz CLI。  

    -m '{"request-id":"{{.RequestNumber}}", "timestamp":"{{.TimestampUnix}}"}'

</br>


Benchmark 打入的 MetaData 就會變成像下面這樣的資料。

```json
{
  "request-id": "1",
  "timestamp": "1544890251"
}
```

</br>


最後附上一個比較完整的調用例子。  

    ghz --insecure \
    --proto ./greeter.proto \
    --call helloworld.Greeter.SayHello \
    -d '{"name":"Joe"}' \
    -m '{"trace_id":"{{.RequestNumber}}", "timestamp":"{{.TimestampUnix}}"}' \
    0.0.0.0:50051

</br>


Link
====
* [Call Template Data - ghz](https://ghz.sh/docs/calldata)
* [Examples - ghz](https://ghz.sh/docs/examples)
