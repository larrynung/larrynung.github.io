---
title: PL/SQL & SQL CODING GUIDELINE 39 - Never use GOTO statements in your code
date: 2017-03-03 13:53:38
tags: [PL/SQL]
keywords: "PL/SQL"
---

條款三十九，從不使用 GOTO 語句。  

<!-- More -->

<br/>


像是下面這樣的程式。  

```psql
...
BEGIN
  ...
  <<check_digit>>
  FOR i IN co_lower_bound .. l_len_array
  LOOP
      <<check_pw_char>>
      FOR j IN co_lower_bound .. l_len_pw
      LOOP
          IF SUBSTR(in_password, j, 1) = SUBSTR(co_digitarray, i, 1) THEN
            l_isdigit := TRUE;
            GOTO check_other_things;
          END IF;
      END LOOP check_pw_char;
  END LOOP check_digit;

  <<check_other_things>>
  NULL;

  IF NOT l_isdigit THEN
    raise_application_error(co_errno, co_errmsg);
  END IF;
END password_check;
...
```

<br/>


可考慮使用 exit 搭配 label 從迴圈內跳離。  

```psql
...
BEGIN
  ...
  <<check_digit>>
  FOR i IN co_lower_bound .. l_len_array
  LOOP
      <<check_pw_char>>
      FOR j IN co_lower_bound .. l_len_pw
      LOOP
          IF SUBSTR(in_password, j, 1) = SUBSTR(co_digitarray, i, 1) THEN
            l_isdigit := TRUE;
            exit check_digit;
          END IF;
      END LOOP check_pw_char;
  END LOOP check_digit;

  <<check_other_things>>
  NULL;

  IF NOT l_isdigit THEN
    raise_application_error(co_errno, co_errmsg);
  END IF;
END password_check;
...
```

<br/>


或是思考是否有其它的寫法，像是上面的程式是用來檢查密碼的，用正規表示式去判斷即可，不需要使用巢狀迴圈。  

```psql
...
BEGIN
  IF NOT REGEXP_LIKE(in_password, co_digitpattern)
  THEN
    raise_application_error(co_errno, co_errmsg);
  END IF;
END password_check;
...
```