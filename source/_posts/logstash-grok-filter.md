---
title: "Logstash - grok filter"
date: 2017-06-05 22:57:37
tags: [Logstash]
---

grok filter 能讓我們使用 Grok 語法簡易的切割 Logstash field。  

<!-- More -->

<br/>


其可使用的設定如下：  

| Setting | Type | Required | Default | Description |
|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| add_field | hash | No | {} | If this filter is successful, add any arbitrary fields to this event. |
| add_tag | array | No | [] | If this filter is successful, add arbitrary tags to the event. |
| break_on_match | boolean | No | true | Break on first match. The first successful match by grok will result in the filter being finished. If you want grok to try all patterns (maybe you are parsing different things), then set this to false. |
| enable_metric | boolean | No | true | Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin. |
| id | string | No | | Add a unique ID to the plugin configuration. If no ID is specified, Logstash will generate one. 
| keep_empty_captures | boolean | No | false | If true, keep empty captures as event fields. |
| match | hash | No | {} | A hash of matches of field ⇒ value |
| named_captures_only | boolean | No | true  | If true, only store named captures from grok. |
| overwrite | array | No | [] | allows you to overwrite a value in a field that already exists. |
| patterns_dir | array | No | [] | |
| patterns_files_glob | string | No | "*" | |
| periodic_flush | boolean | No | false | Call the filter flush method at regular interval. |
| remove_field | array | No | [] | If this filter is successful, remove arbitrary fields from this event. |
| remove_tag | array | No | [] | If this filter is successful, remove arbitrary tags from the event. |
| tag_on_failure | array | No | ["_grokparsefailure"] | Append values to the tags field when there has been no successful match |
| tag_on_timeout | string | No |  "_groktimeout" | Tag to apply if a grok regexp times out. |
| timeout_millis | number | No | 30000 | Attempt to terminate regexps after this amount of time. |

<br/>


最常用的就是 match 設定，可用 Grok 語法設定要如何將 message 切出 Logstash field。像是下面這邊設定訊息是由 IP、WORD、URIPATHPARAM、NUMBER、NUMBER 所組成，如果符合這樣組成的訊息，則依序將資料拆分為 client、 method、 request、 bytes、 duration 這幾個 Logstash field。   

    /opt/logstash/bin/logstash -e 'input { stdin{} } filter { grok { match => { "message" => "%{IP:client} %{WORD:method} %{URIPATHPARAM:request} %{NUMBER:bytes} %{NUMBER:duration}" } } } output { stdout { codec => rubydebug } }'

{% asset_img 1.png %}

<br/>


match 設定可以一次設定多組，預設會依序照設定處理，如果訊息滿足設定條件，則會終止向下處理。但有的時候我們會希望讓 Logstash 跑完所有的設定，這時可以將 break_on_match 設為 false。  

    /opt/logstash/bin/logstash -e 'input { stdin{} } filter { grok { break_on_match => false match => { "message" => "%{GREEDYDATA:messagebody}" } match => { "message" => "%{IP:client} %{WORD:method} %{URIPATHPARAM:request} %{NUMBER:bytes} %{NUMBER:duration}" } } } output { stdout { codec => rubydebug } }'

{% asset_img 2.png %}

<br/>


如果要在 Grok 設定滿足時順帶設定額外的 Logstash field，可使用 add_field 設定。  

    /opt/logstash/bin/logstash -e 'input { stdin{} } filter { grok {  match => { "message" => "%{IP:client} %{WORD:method} %{URIPATHPARAM:request} %{NUMBER:bytes} %{NUMBER:duration}" } add_field => { "msg" => "Hello World" } } } output { stdout { codec => rubydebug } }'

{% asset_img 3.png %}

<br/>


如果要增設額外的 Logstash tag，則使用 add_tag 設定。  

    /opt/logstash/bin/logstash -e 'input { stdin{} } filter { grok {  match => { "message" => "%{IP:client} %{WORD:method} %{URIPATHPARAM:request} %{NUMBER:bytes} %{NUMBER:duration}" } add_tag => { "msg" => "Hello World" } } } output { stdout { codec => rubydebug } }'

{% asset_img 4.png %}

<br/>


如果要將現有的 Logstash field 覆蓋，可使用 overwrite 設定。  

    /opt/logstash/bin/logstash -e 'input { stdin{} } filter { grok {  match => { "message" => "%{IP:message}" } overwrite => ["message"] } } output { stdout { codec => rubydebug } }'

{% asset_img 5.png %}

<br/>


Link
----
* [grok | Logstash Reference [5.4] | Elastic](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html)
