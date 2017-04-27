---
title: Filebeat - Configuring Filebeat
date: 2017-04-27 13:23:52
tags: [Filebeat]
---

Filebeat 的設定檔為 filebeat.yml，可以設定資料的輸入與輸出，以及其它細項設定。  

<!-- More -->

<br/>


像是設定資料的輸入，這邊可以指定要輸入的 Log 檔位置。  

{% codeblock lang:yaml %}
filebeat.prospectors:

- input_type: log
  paths:
    - E:\AgileSlot\Log\*\*Full*log*
{% endcodeblock %}

<br/>


可以設定 Log 資料要怎樣切割傳送，像筆者使用 Log4Net 去記錄 Log，Log 前面一定會有 Log 的時間，就可以以 Log 時間當作切割傳送的依據。  

{% codeblock lang:yaml %}
filebeat.prospectors:

- input_type: log
  # The regexp Pattern that has to be matched. The example pattern matches all lines starting with [
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'

  # Defines if the pattern set under pattern should be negated or not. Default is false.
  multiline.negate: true

  # Match can be set to "after" or "before". It is used to define if lines should be append to a pattern
  # that was (not) matched before or after or as long as a pattern is not matched based on negate.
  # Note: After is the equivalent to previous and before is the equivalent to to next in Logstash
  multiline.match: after
{% endcodeblock %}
  
<br/>


可以設定多久以前的 Log 不要傳送，這設定在 Log 檔很多時特別重要，不做這設定可能會傳送過多的 Log，導致記憶體吃過凶。  

{% codeblock lang:yaml %}
filebeat.prospectors:

- input_type: log
  ignore_older: 24h
{% endcodeblock %}
  
<br/>


可設定資料的輸出，以送到 Logstash 為例，可以設定 Logstash 位置、每個 Logstash 要用幾個 worker 處理、資料壓縮的等級、是否負載平衡、及 Index 等。  

{% codeblock lang:yaml %}
output.logstash:
 
  # The Logstash hosts
  hosts: ["172.16.49.172:5044","172.16.49.116:5044"]

  # Number of workers per Logstash host.
  worker: 2

  # Set gzip compression level.
  #compression_level: 3

  # Optional load balance the events between the Logstash hosts
  loadbalance: true

  # Number of batches to be send asynchronously to logstash while processing
  # new batches.
  #pipelining: 0

  # Optional index name. The default index name is set to name of the beat
  # in all lowercase.
  index: "cas-agileslot-dev"
{% endcodeblock %}
  
<br/>


也可以設定 Filebeat 的 Log，設定是否寫到檔案、檔案位置...等。

{% codeblock lang:yaml %}
# Logging to rotating files files. Set logging.to_files to false to disable logging to
# files.
logging.to_files: true
logging.files:
  # Configure the path where the logs are written. The default is the logs directory
  # under the home path (the binary location).
  #path: /var/log/filebeat
  
  # The name of the files where the logs are written to.
  #name: filebeat
{% endcodeblock %}
  
<br/>


完整的設定範例如下：  

{% codeblock lang:yaml %}
##################$$$###### Filebeat Configuration ############################

# This file is a full configuration example documenting all non-deprecated
# options in comments. For a shorter configuration example, that contains only
# the most common options, please see filebeat.yml in the same directory.
#
# You can find the full configuration reference here:
# https://www.elastic.co/guide/en/beats/filebeat/index.html

#=========================== Filebeat prospectors =============================

# List of prospectors to fetch data.

filebeat.prospectors:

- input_type: log
  paths:
    - E:\AgileSlot\Log\*\*Full*log*

  # The regexp Pattern that has to be matched. The example pattern matches all lines starting with [
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'

  # Defines if the pattern set under pattern should be negated or not. Default is false.
  multiline.negate: true

  # Match can be set to "after" or "before". It is used to define if lines should be append to a pattern
  # that was (not) matched before or after or as long as a pattern is not matched based on negate.
  # Note: After is the equivalent to previous and before is the equivalent to to next in Logstash
  multiline.match: after
  
  ignore_older: 24h
#----------------------------- Logstash output --------------------------------
output.logstash:
 
  # The Logstash hosts
  hosts: ["172.16.49.172:5044","172.16.49.116:5044"]

  # Number of workers per Logstash host.
  worker: 2

  # Set gzip compression level.
  #compression_level: 3

  # Optional load balance the events between the Logstash hosts
  loadbalance: true

  # Number of batches to be send asynchronously to logstash while processing
  # new batches.
  #pipelining: 0

  # Optional index name. The default index name is set to name of the beat
  # in all lowercase.
  index: "cas-agileslot-dev"
  
shipper:
  tags: ["CAS","AgileSlot","DEV"]


# Logging to rotating files files. Set logging.to_files to false to disable logging to
# files.
logging.to_files: true
logging.files:
  # Configure the path where the logs are written. The default is the logs directory
  # under the home path (the binary location).
  #path: /var/log/filebeat
  
  # The name of the files where the logs are written to.
  #name: filebeat
{% endcodeblock %}
  
<br/>
  
  
如果資料可能有多個輸入，設定這邊可用上述介紹的方式撰寫，只要設定多組 paths。但若想更好維護與管理，建議是使用 filebeat.config_dir 來將設定做個切分。  

<br/>

像是在 filebeat.yml 設定檔中保留輸出與 Filebeat Log 的設定，並在上面用 config_dir 設定其它設定檔存放的位置。  
  
{% codeblock lang:yaml %}
filebeat.config_dir: configs

#----------------------------- Logstash output --------------------------------
output.logstash:
 
  # The Logstash hosts
  hosts: ["172.16.49.172:5044","172.16.49.116:5044"]

  # Number of workers per Logstash host.
  worker: 2

  # Set gzip compression level.
  #compression_level: 3

  # Optional load balance the events between the Logstash hosts
  loadbalance: true

  # Number of batches to be send asynchronously to logstash while processing
  # new batches.
  #pipelining: 0

  # Optional index name. The default index name is set to name of the beat
  # in all lowercase.
  index: "cas-agileslot-dev"


# Logging to rotating files files. Set logging.to_files to false to disable logging to
# files.
logging.to_files: true
logging.files:
  # Configure the path where the logs are written. The default is the logs directory
  # under the home path (the binary location).
  #path: /var/log/filebeat
  
  # The name of the files where the logs are written to.
  #name: filebeat
{% endcodeblock %}

<br/>


將輸入的設定部份移至所設定的目錄內即可。  

{% asset_img 1.png %}

<br/>

  
{% codeblock lang:yaml %}
  ##################$$$###### Filebeat Configuration ############################

# This file is a full configuration example documenting all non-deprecated
# options in comments. For a shorter configuration example, that contains only
# the most common options, please see filebeat.yml in the same directory.
#
# You can find the full configuration reference here:
# https://www.elastic.co/guide/en/beats/filebeat/index.html

#=========================== Filebeat prospectors =============================

# List of prospectors to fetch data.

filebeat.prospectors:

- input_type: log
  paths:
    - E:\AgileSlot\Log\*\*Full*log*
  exclude_files: ["\.zip$","\.7z$"]
  
  document_type: applog

  # The regexp Pattern that has to be matched. The example pattern matches all lines starting with [
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'

  # Defines if the pattern set under pattern should be negated or not. Default is false.
  multiline.negate: true

  # Match can be set to "after" or "before". It is used to define if lines should be append to a pattern
  # that was (not) matched before or after or as long as a pattern is not matched based on negate.
  # Note: After is the equivalent to previous and before is the equivalent to to next in Logstash
  multiline.match: after
  
  ignore_older: 24h
{% endcodeblock %}

<br/>
  

Link
----
* [Step 2: Configuring Filebeat | Filebeat Reference [5.3] | Elastic](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-configuration.html)
* [Step 3: Configuring Filebeat to Use Logstash | Filebeat Reference [5.3] | Elastic](https://www.elastic.co/guide/en/beats/filebeat/current/config-filebeat-logstash.html)