---
title: Node.js - Transform stream
date: 2018-07-30 23:13:42
tags: [Node.js]
---

Transform stream 可以將輸入串流的資料讀入，將讀入的內容轉換，然後輸出到輸出串流。  

<!-- More -->

<br/>


像是內建的 Gzip transform stream 就能將輸入的資料做 Gzip 壓縮然後輸出。  

```js
const zlib = require('zlib');
const gzip = zlib.createGzip();
const fs = require('fs');
const input = fs.createReadStream('index.js');
const output = fs.createWriteStream('index.js.gz');

input.pipe(gzip).pipe(output);
```

<br/>


如果要自行撰寫 Transform stream，我們可以撰寫個繼承自 Transform 的類別，然後在 _transform 內撰寫每次收到資料要做的處理，以及在 _flush 內撰寫清空緩衝區時要做的處理，在撰寫這兩個方法時，如果資料轉換完畢，可以用 this.push 將資料輸出。如果處理完成，則要記得調用 callback 方法。  

```js
'use strict';

const Transform = require('stream').Transform;

class MyTransformStream extends Transform {  
    _transform(data, encoding, callback) {
        ...
        //this.push(data);
        ...
        callback();
    }

    _flush(callback) {
        ...
        //this.push(data);
        ...
        callback();
    }
}
```

<br/>


像是筆者寫的這隻 AnalyzeStream，其功能為將 HTML 輸入，依照檢查的 Rule 分析，最後將分析的結果輸出。因為要分析的資料需要完整的 HTML，所以 _transform 這邊只有很簡單的將收到的資料存放起來，然後調用 callback 告知處理完成。在 _flush 這邊會將存放的資料套用 Rule 分析，將分析的結果用 this.push 輸出，最後調用 callback 告知處理完成。    

```js
'use strict';

const Transform = require('stream').Transform;
const cheerio = require('cheerio');

/**
 * The transform stream for analyze with rules
 */
class AnalyzeStream extends Transform {
    /**
     * @constructor
     * @param {*} rules
     * @param {*} callback
     */
    constructor(rules, callback) {
        super();
        this._rules = rules;
        this._data = '';
        this._callback = callback;
    }

    /**
     * @param {*} data
     * @param {*} encoding
     * @param {*} callback
     */
    _transform(data, encoding, callback) {
        this._data += data.toString();
        callback();
    }

    /**
     * @param {*} callback
     */
    _flush(callback) {
        let dom = cheerio.load(this._data);
        let result = true;
        let messages = [];
        Object.keys(this._rules).forEach((element) => {
            let rule = this._rules[element];
            if (rule.isActive) {
                let ruleCheck = rule.check(dom);
                result = result && ruleCheck.result;
                if (!ruleCheck.result) {
                    this.push(ruleCheck.message + '\n');
                    messages.push(ruleCheck.message);
                }
            }
        });
        this._data = '';
        callback();
        this._callback(result, messages);
    }
}

module.exports = AnalyzeStream;
```

Link
----
* [打造自己的 Node.js Transform Stream](http://fred-zone.blogspot.com/2017/09/nodejs-transform-stream.html)
* [How to create transform streams for manipulating data with Node.js - a programming tutorial for web developers | CodeWinds](http://codewinds.com/blog/2013-08-20-nodejs-transform-streams.html)
