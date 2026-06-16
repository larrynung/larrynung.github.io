---
title: "GAE's Users Service"
date: "2013-11-06 12:00:00"
description: "開發GAE application時可能會有整合Google帳號的需求，這時我們可以使用Users Service。 首先將google.appengine.api.users import進來。 呼叫users.get_current_user()取得當前的使用者。"
---

開發GAE application時可能會有整合Google帳號的需求，這時我們可以使用Users Service。

首先將google.appengine.api.users import進來。

```python
from google.appengine.api import users
```

呼叫users.get_current_user()取得當前的使用者。

```python
user = users.get_current_user()
```

若是有取到當前的使用者，代表目前使用者已是登入的狀態，我們可以取得使用者資訊做些呈現 (可參閱User 類別這篇)。

像是呼叫nickname方法取得當前使用者的暱稱。

```python
nickName = user.nickname()
```

呼叫email方法取得當前使用者的Email位置。

```python
email = user.email()
```

或者是呼叫user_id方法取得當前使用者的識別ID。

```python
userID = user.user_id()
```

若需要實現登出的動作，則我們可以呼叫create_logout_url方法取得登出動作的網址，。

```python
users.create_logout_url("/")
```

而要是使用者尚未登入，這邊我們無法取得當前的使用者，這時可以透過users.create_login_url方法取得登入的頁面位置，呼叫users.create_login_url的同時可以指定登入成功所要返回的頁面位置。

```python
users.create_login_url(self.request.uri)
```

登入的頁面位置取得後，視需求可以做些不同的處理，像是讓使用者透過點擊連結去做登入，或是直接將頁面直接導過去。

```python
self.redirect(users.create_login_url(self.request.uri))
```

總結下來整個Users Service的撰寫應該會是像下面這樣的處理方式：

```python
    	user = users.get_current_user()

    	if user:
    		#User Logined
    	else:
		#User Need Login => Redirect to login page
    		self.redirect(users.create_login_url(self.request.uri))
```

最後這邊實際來看個完整的範例程式：

本地運行起來可以看到像下面這樣簡易的登入畫面，按下Login按鈕繼續。

![image_thumb.png](/images/posts/dd434fd1-e8bf-48d5-9df8-551c2f5cd471/image_thumb.png)

會看到登入成功後的樣子，這邊的範例是將NickName與登出功能秀出來。

![image_thumb_1.png](/images/posts/dd434fd1-e8bf-48d5-9df8-551c2f5cd471/image_thumb_1.png)

本地測試時帳號怎樣輸入都會成功登入，因為只是讓我們可以很容易的在本地進行測試，不會整合Google的帳號服務，也不會進行驗證的動作。但若是實際將其佈署到Cloud上，就會與Google帳號服務整合，所以可以看到登入的畫面會改成Google帳號的登入頁面。

![image_thumb_3.png](/images/posts/dd434fd1-e8bf-48d5-9df8-551c2f5cd471/image_thumb_3.png)

登入後的動作一樣正常運作。

![image_thumb_2.png](/images/posts/dd434fd1-e8bf-48d5-9df8-551c2f5cd471/image_thumb_2.png)

## Link

* Using the Users Service
