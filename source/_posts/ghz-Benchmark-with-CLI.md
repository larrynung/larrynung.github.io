---
title: ghz - Benchmark with CLI
date: 2019-07-08 19:46:47
tags: [ghz]
---

要用 ghz CLI 打 Benchmark，可先參考 ghz CLI 的使用說明。  

<!-- More -->

```
usage: ghz [<flags>] [<host>]

Flags:
  -h, --help                Show context-sensitive help (also try --help-long and --help-man).
      --config=             Path to the JSON or TOML config file that specifies all the test run settings.
      --proto=              The Protocol Buffer .proto file.
      --protoset=           The compiled protoset file. Alternative to proto. -proto takes precedence.
      --call=               A fully-qualified method name in 'package.Service/method' or 'package.Service.Method' format.
  -i, --import-paths=       Comma separated list of proto import paths. The current working directory and the directory of the protocol buffer file are automatically added to the import list.
      --cacert=             File containing trusted root certificates for verifying the server.
      --cert=               File containing client certificate (public key), to present to the server. Must also provide -key option.
      --key=                File containing client private key, to present to the server. Must also provide -cert option.
      --cname=              Server name override when validating TLS certificate - useful for self signed certs.
      --skipTLS             Skip TLS client verification of the server's certificate chain and host name.
      --insecure            Use plaintext and insecure connection.
      --authority=          Value to be used as the :authority pseudo-header. Only works if -insecure is used.
  -c, --concurrency=50      Number of requests to run concurrently. Total number of requests cannot be smaller than the concurrency level. Default is 50.
  -n, --total=200           Number of requests to run. Default is 200.
  -q, --qps=0               Rate limit, in queries per second (QPS). Default is no rate limit.
  -t, --timeout=20          Timeout for each request in seconds. Default is 20, use 0 for infinite.
  -z, --duration=0          Duration of application to send requests. When duration is reached, application stops and exits. If duration is specified, n is ignored. Examples: -z 10s -z 3m.
  -x, --max-duration=0      Maximum duration of application to send requests with n setting respected. If duration is reached before n requests are completed, application stops and exits.
                            Examples: -x 10s -x 3m.
      --connections=1       Number of connections to use. Concurrency is distributed evenly among all the connections. Default is 1.
  -d, --data=               The call data as stringified JSON. If the value is '@' then the request contents are read from stdin.
  -D, --data-file=          File path for call data JSON file. Examples: /home/user/file.json or ./file.json.
  -b, --binary              The call data comes as serialized binary message or multiple count-prefixed messages read from stdin.
  -B, --binary-file=        File path for the call data as serialized binary message or multiple count-prefixed messages.
  -m, --metadata=           Request metadata as stringified JSON.
  -M, --metadata-file=      File path for call metadata JSON file. Examples: /home/user/metadata.json or ./metadata.json.
      --stream-interval=0   Interval for stream requests between message sends.
      --reflect-metadata=   Reflect metadata as stringified JSON used only for reflection request.
  -o, --output=             Output path. If none provided stdout is used.
  -O, --format=             Output format. One of: summary, csv, json, pretty, html, influx-summary, influx-details. Default is summary.
      --connect-timeout=10  Connection timeout in seconds for the initial connection dial. Default is 10.
      --keepalive=0         Keepalive time in seconds. Only used if present and above 0.
      --name=               User specified name for the test.
      --tags=               JSON representation of user-defined string tags.
      --cpus=8              Number of cpu cores to use.
  -v, --version             Show application version.

Args:
  [<host>]  Host and port to test.
```

</br>


比較常用的有 --proto、--call、-d、-c、-n、--connections、-O、-o 這幾個參數。  

</br>


像是要打一個 Benchmark 就會用 --proto 指定 proto 檔的位置、用 --call 指定要調用哪個 proto service、-d 指定 proto service 調用時所需要的資料、-c 指定 Benchmark 的 concurrent 數、-n 指定 Benchmark 要發送的數量，最後帶上 gRPC service 的 IP。  

    ghz --proto $protofile --call $protoservice -d '$protodata' -c $concurrency -n $numbers --insecure $ip

{% asset_img 1.png %}

</br>


運行的結果有點類似 Apache 的 ab，可看到處理時間的統計與分佈。  

</br>


如果要設定 Benchmark 的 gRPC 連線數，可使用 --connections 指定。若不指定預設是使用一個 gRPC 連線，不論設多少的 Concurrent 都共用這條連線。  

ghz --proto $protofile --call $protoserv    ice -d '$protodata' --connections $connections -c $concurrency -n $numbers --insecure $ip

{% asset_img 2.png %}

</br>


除了直接 Console 顯示 Benchmark 的結果，ghz 也提供了輸出成報表檔的功能，支援輸出 json 、html、csv、… 等格式，可透過 -O 指定輸出的格式，並透過 -o 指定輸出檔案的位置。  

    ghz --proto $protofile --call $protoservice -d '$protodata' -c $concurrency -n $numbers --insecure $ip -O html -o $outputfile

{% asset_img 3.png %}

</br>
