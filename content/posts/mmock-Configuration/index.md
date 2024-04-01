---
title: "mmock - Configuration"
date: "2017-09-17 23:32:15"
tags: [mmock]
---


使用 mmock 去 Mock API，會需要放置 mock 的設定。  

<!-- More -->

<br/>


設定檔可以是 json 格式...

    {
        "request": {
            "method": "GET",
            "path": "/hello/*"
        },
        "response": {
            "statusCode": 200,
            "headers": {
                "Content-Type":["application/json"]
            },
            "body": "{\"hello\": \"{{request.query.name}}, my name is {{fake.FirstName}}\"}"
        }
    }  

<br/>


也可以是 yml 格式...

    ---
    request:
      method: GET
      path: "/hello/*"
    response:
      statusCode: 200
      headers:
        Content-Type:
        - application/json
      body: '{"hello": "{{request.query.name}}, my name is {{fake.FirstName}}"}'

<br/>


設定檔格式定義如下：  

    {
    	"description": "Some text that describes the intended usage of the current configuration",
    	"request": {
    		"host": "example.com",
    		"method": "GET|POST|PUT|PATCH|...",
    		"path": "/your/path/:variable",
    		"queryStringParameters": {
    			"name": ["value"],
    			"name": ["value", "value"]
    		},
    		"headers": {
    			"name": ["value"]
    		},
    		"cookies": {
    			"name": "value"
    		},
    		"body": "Expected Body"
    	},
    	"response": {
    		"statusCode": "int (2xx,4xx,5xx,xxx)",
    		"headers": {
    			"name": ["value"]
    		},
    		"cookies": {
    			"name": "value"
    		},
    		"body": "Response body"
    	},
    	"control": {
    		"scenario": {
    			"name": "string (scenario name)",
    			"requiredState": [
    				"not_started (default state)",
    				"another_state_name"
    			],
    			"newState": "new_stat_neme"
    		},
    		"proxyBaseURL": "string (original URL endpoint)",
    		"delay": "int (response delay in seconds)",
    		"crazy": "bool (return random 5xx)",
    		"priority": "int (matching priority)",
    		"webHookURL" : "string (URL endpoint)"
    	}
    }

<br/>


主要分為 Request、Response、與 Control 幾塊。  

<br/>


Request 這塊是用來描述 http 請求的，像是請求的主機、http method、請求的路徑位置、請求的參數、請求的標頭、cookie、及請求的內容。  

| Element | Description |
|:-------------:|:-------------:|
| host | Request http hostt. (without port)  |
| method  | Request http method. |
| path | Resource identifier. It allows :value matching. Mandatory |
| queryStringParameters | Array of query strings. It allows more than one value for the same key. |
| headers | Array of headers. It allows more than one value for the same key. |
| cookies | Array of cookies. |
| body | Body string. It allows * pattern. |

<br/>


Response 部分用來描述 http 的回應，像是回應的狀態碼、回應的標頭、cookie、及回應的內容。  

| Element | Description |
|:-------------:|:-------------:|
| statusCode | Request http method. |
| headers | Array of headers. It allows more than one value for the same key and vars. |
| cookies | Array of cookies. It allows vars. |
| body | Body string. It allows vars. |

<br/>


Control 部分不一定需要，用來做些控制使用的，像是回應的延遲時間、是否隨機回應錯誤...等。  

| Element | Description |
|:-------------:|:-------------:|
| scenario | A scenario is essentially a state machine whose states can be arbitrarily assigned. |
| proxyBaseURL | If this parameter is present, it sends the request data to the BaseURL and resend the response to de client.  |
| delay | Delay the response in seconds. Simulate bad connection or bad server performance. |
| crazy | Return random server errors (5xx) in some request. Simulate server problems. |
| priority | Set the priority to avoid match in less restrictive mocks. Higher, more priority. |
| webHookURL | After any match if this option is defined it will notify the match to the desired endpoint. |

<br/>


Link
----
* [jmartin82/mmock: Mmock is an HTTP mocking application for testing and fast prototyping](https://github.com/jmartin82/mmock)
