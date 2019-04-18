---
title: gRPC - Protocol Buffers/gRPC Integration Into .NET Build
date: 2019-04-18 00:56:32
tags: [gRPC]
---

Grpc.Tools 在 1.17 後我們可以將 proto 檔的編譯動作直接整到 dotnet build。使用上只要在專案檔中加上 <Protobuf> 設定即可。    

<!-- More -->

<br/>


像是筆者這邊準備了一個 GRPC.Message 專案，proto 檔放在上上層的 proto 目錄下。  

.
|___ proto
|  |___ message.proto
|  |___ service.proto
|___ src
   |___ GRPC.Message

<br/>


那在 GRPC.Message 的專案檔中可以像下面這樣設定。  

```C#
...
<ItemGroup>
    <Protobuf Include="../../**/*.proto" OutputDir="." CompileOutputs="false" GrpcService="both" />
</ItemGroup>
...
```

{% asset_img 1.png %}

<br/>


設定好後建置專案。  

{% asset_img 2.png %}

<br/>


proto 檔就會被編譯成對應的程式碼。  

{% asset_img 3.png %}

<br/>


Link
----
* [Protocol Buffers/gRPC Integration Into .NET Build](https://chromium.googlesource.com/external/github.com/grpc/grpc/+/HEAD/src/csharp/BUILD-INTEGRATION.md)
