---
layout: post
title: "SQL Server - Change Collation"
date: 2014-03-21 23:04:00
comments: true
categories: SQL 
keywords: "SQL, Collation"
description: "SQL Server - Change Collation"
---

要變更 Database Collation ，可以透過 GUI 開啟 Database Property 去調整 Collation 欄位值。  

<!-- More -->

在調整之前必需先將 Restrict Access 欄位值為 SINGLE_USER，不然會無法切換 Collation。  

{% img /images/posts/ChangeSqlCollation/1.png %}

<br/>

透過 GUI 設定是比較簡易，但是資料庫一多就不怎麼適用，這時可以用 SQL 語法來做處理，開啟一個新的 Query ，填入下列語法，修改 Collation name，接著依序針對不同的資料庫下去執行就可以了。

{% codeblock lang:sql %}
declare @dbname varchar (100)
set @dbname= quotename(db_name ())
set @collationName = 'SQL_Latin1_General_CP1_CI_AS'
exec('ALTER DATABASE ' + @dbname + ' SET SINGLE_USER WITH ROLLBACK IMMEDIATE');
exec('ALTER DATABASE ' + @dbname + ' COLLATE ' + @collationName);
exec('ALTER DATABASE ' + @dbname + ' SET MULTI_USER');
{% endcodeblock %}

<br/>

變更 Column 的 Collation 比較麻煩一點，雖然一樣可以用 GUI 去做切換，但欄位一多這方法也不怎麼適用。這時一樣得改用 SQL 語法來做處理，開啟一個新的 Query ，填入下列語法 ，修改 Collation name 後運行，即會自動產生出所有資料表內的 Column Collation 轉換語法，將之依序帶入 SQL Query 視窗運行即可。這邊比較麻煩的是若有設定PK、FK之類的，需先抽掉才能轉換。

{% codeblock lang:sql %}
declare @TableName Nvarchar (4000),
      @ColumnName Nvarchar(4000 ),
      @CharacterMaxLen Nvarchar(4000 ),
      @CollationName Nvarchar(4000 ),
      @IsNullable Nvarchar(4000 ),
      @DataType Nvarchar(4000 ),
      @SQLText Nvarchar(4000 )
 
SET @CollationName = 'SQL_Latin1_General_CP1_CI_AS'
 
declare MyTableCursor cursor for
       SELECT name FROM sys. Tables
 
OPEN MyTableCursor


FETCH NEXT FROM MyTableCursor INTO @TableName
WHILE @@FETCH_STATUS = 0
    BEGIN
        DECLARE MyColumnCursor Cursor
        FOR
        SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH ,
            IS_NULLABLE from information_schema .columns
            WHERE table_name = @TableName AND  (Data_Type LIKE '%char%'
            OR Data_Type LIKE '%text%') AND COLLATION_NAME <> @CollationName
            ORDER BY ordinal_position
        Open MyColumnCursor


        FETCH NEXT FROM MyColumnCursor INTO @ColumnName, @DataType,
              @CharacterMaxLen , @IsNullable
        WHILE @@FETCH_STATUS = 0
            BEGIN
            SET @SQLText = 'ALTER TABLE ' + @TableName + ' ALTER COLUMN [' + @ColumnName + '] ' +
              @DataType + '(' + CASE WHEN @CharacterMaxLen = -1 THEN 'MAX' ELSE @CharacterMaxLen END +
              ') COLLATE ' + @CollationName + ' ' +
              CASE WHEN @IsNullable = 'NO' THEN 'NOT NULL' ELSE 'NULL' END
            PRINT @SQLText


        FETCH NEXT FROM MyColumnCursor INTO @ColumnName, @DataType,
              @CharacterMaxLen , @IsNullable
        END
        CLOSE MyColumnCursor
        DEALLOCATE MyColumnCursor


FETCH NEXT FROM MyTableCursor INTO @TableName
END
CLOSE MyTableCursor
DEALLOCATE MyTableCursor
{% endcodeblock %}
