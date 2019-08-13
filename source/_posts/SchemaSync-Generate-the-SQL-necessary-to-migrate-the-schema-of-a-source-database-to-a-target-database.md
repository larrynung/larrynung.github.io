---
title: >-
  SchemaSync - Generate the SQL necessary to migrate the schema of a source
  database to a target database
date: 2019-08-13 07:38:57
tags: [SchemaSync]
---

SchemaSync 使用方式如下:  

<!-- More -->

    schemasync [options] <source> <target>
    
    # source/target format: mysql://user:pass@host:port/database
    # output format: <database>[_<tag>].YYYYMMDD.(patch|revert)[_<version>].sql
    -h, --help            show this help message and exit
    -V, --version         show version and exit.
    -r, --revision        increment the migration script version number
                          if a file with the same name already exists.
    -a, --sync-auto-inc   sync the AUTO_INCREMENT value for each table.
    -c, --sync-comments   sync the COMMENT field for all tables AND columns
    --tag=TAG             tag the migration scripts as <database>_<tag>.
                          Valid characters include [A-Za-z0-9-_]
    --output-directory=OUTPUT_DIRECTORY
                          directory to write the migration scrips.
                          The default is current working directory.
                          Must use absolute path if provided.
    --log-directory=LOG_DIRECTORY
                          set the directory to write the log to.
                          Must use absolute path if provided.
                          Default is output directory.
                          Log filename is schemasync.log

</br>


簡單的說就是帶入來源資料庫位置與目的資料庫位置，SchemaSync 即會連入來源與目的資料庫進行比對，產生對應的腳本檔案。  

</br>


其它像是帶入 -r 參數增加腳本檔案的版本號、帶入 -c 參數指定連帶 Comment 一起產進腳本、帶入 --tag 參數指定腳本檔案的 Tag 部份。  

</br>


這邊實際運行看看，可看到跑完後會產生了一個 patch 用的腳本，一個是 revert 用的腳本。  

{% asset_img 1.png %}

</br>


如果 patch 的腳本是新增資料表。  

{% asset_img 2.png %}

</br>


那 revert 的腳本就會是刪除資料表。  

{% asset_img 3.png %}

</br>


如果 source 與 target 資料庫位置互換，那產出來的腳本也會跟著互換。  

{% asset_img 4.png %}

</br>


{% asset_img 5.png %}

</br>


{% asset_img 6.png %}
