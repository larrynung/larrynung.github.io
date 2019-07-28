---
title: Redis - A simple syntax to describe how data stored
date: 2019-07-28 22:16:23
tags: [Redis]
---

在使用 redis 時，資料怎樣在 redis 內存放常會需要設計，或是需要拿出來跟團隊溝通討論。用畫圖表述或是列表有點不方便，redis 資料結構豐富也不是很好表示。    

<!-- More -->

</br>


這邊筆者嘗試定義簡易的表示方式。  

</br>


String 型態表示方式...

    $string-key => $string-value

</br>


HaHash 型態表示方式...

    $hash-key => {
        {$field-key, $field-value},
        ...
    }


</br>


List 型態表示方式...

    $list-key => [
        $list-value,
        ...
    ]


</br>


Set 型態表示方式...

    $set-key => {
        $set-value,
        ...
    }

</br>


SortedSet 表示方式...

    $sorted-set-key => {
        ($score, $set-value),
        ...
    }

</br>


像是 Redis reliable queue 那篇的設計...

{% asset_img 1.png %}


</br>


用這樣的表示方式設計就會變成這樣:  

    pending => [$data-id, ...]
    working:$worker-id => [$data-id, ...]
    value => {
        {$data-id, $data},
        ...
    }

</br>


使用情境的描述就會像下面這樣: 

    pending => [6, 5]
    working:1 => [2, 1]
    working:2 => [4, 3]
    value => {
        {1, "{\"Name\": \"Larry\"}"},
        {2, "{\"Name\": \"Tom\"}"},
        {3, "{\"Name\": \"Bob\"}"},
        {4, "{\"Name\": \"John\"}"},
        {5, "{\"Name\": \"Ryan\"}"},
        {6, "{\"Name\": \"Andrew\"}"},
    }
