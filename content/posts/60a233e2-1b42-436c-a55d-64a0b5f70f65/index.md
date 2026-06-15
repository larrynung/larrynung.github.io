---
title: "GAE's Mail Python API"
date: "2013-11-06 12:00:00"
description: "GAE's Mail Python API"
tags: [Python]
---

GAE提供Mail API可供開發人員撰寫寄信程式，這邊以Python為例稍微紀錄一下

首先將google.appengine.api.mail import進來。

```python
from google.appengine.api import mail
```

mail.is_email_valid可以檢驗email的格式是否正確，但是筆者試驗是如Issue 7471:mail.is_email_valid returns True for invalid email addresses and URLs這邊網友所回報的一樣沒有效果。

```python
var isValid = mail.is_email_valid(emailAddress)
```

mail.send_mail可以用來發送電子郵件，只要帶入寄件者、收件者、主旨、以及信件內文。基於安全理由，訊息的寄件者地址必須是應用程式管理員的電子郵件地址，或是已登入使用者的「Google 帳戶」電子郵件地址，。

```python
mail.send_mail(sender, receiver, subject, message)
```

最後這邊實際來看個完整的範例程式：

將範例程式佈署至Cloud，在Application的網址後面帶入sender、receiver、subject、以及message這幾個參數。沒意外的話信件就會照我們給的資訊發送出去。

![image_thumb_1.png](/images/posts/60a233e2-1b42-436c-a55d-64a0b5f70f65/image_thumb_1.png)

![image_thumb_2.png](/images/posts/60a233e2-1b42-436c-a55d-64a0b5f70f65/image_thumb_2.png)

## Link

* Mail Python API Overview - Google App Engine — Google Developers
