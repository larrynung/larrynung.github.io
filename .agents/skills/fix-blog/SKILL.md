---
name: fix-blog
description: 檢查並修正部落格文章問題
---

# Blog Fix Skill

檢查並修正部落格文章問題

## 觸發条件

當使用者要求檢查部落格文章問題時使用此 skill。

## 問題類型

1. **圖片連結問題** - 舊語法在 Hugo 中無法顯示
   - `{% img /images/posts/xxx.png %}` → 需轉換為 Markdown 語法
2. **HTML 格式問題** - 需轉換為 Markdown
   - `<h1>`-`<h6>` 標題 → `#` - `######`
   - `<pre><code>` 代碼區塊 → ``` ```
   - `<a href="...">` 連結 → `[text](url)`
   - `<strong>`/`<b>` 粗體 → `**text**`
   - `<em>`/`<i>` 斜體 → `*text*`
   - `<ul>`/`<ol>` 清單 → `-` / `1.`
3. **格式問題** - 標題分隔線、代碼區塊
   - `----` 標題分隔線
   - 4+ 空格縮進的代碼未用 ``` 包裹

## 處理範圍

只處理 Hugo 文章目錄：`content/posts/`

### 處理流程

### Step 1: 分析問題

使用 grep 分析文章，找出有問題的語法：

```bash
# 找出舊圖片語法
rg -l '\{% img' content/posts/ -g '*.md'

# 找出標題分隔線
rg -l '^----$' content/posts/ -g '*.md'

# 找出可能未包裹的代碼（4+ 空格縮進）
rg -n '^\s{4,}[a-zA-Z]' content/posts/ -g '*.md'
```

### Step 2: 修復問題

每次選擇一篇文章進行修復：
1. 讀取文章內容
2. 識別問題語法
3. 確認圖片文件存在
4. 進行替換
5. 驗證修復

#### 圖片語法替換
```
{% img /images/posts/NAME.png %} → ![NAME](/images/posts/NAME.png)
```

⚠️ 避免使用 replaceAll，務必逐一確認替換正確

**圖片路徑差異**：
- `{% img /images/posts/xxx}` → `/images/posts/xxx`（絕對路徑）
- `![alt](images/xxx.png)` → 相對路徑（文章目錄下的 images/ 資料夾）

#### 預防批量替換問題
使用 replaceAll 可能導致殘留字元（如 `%}`），務必逐行確認

#### 確認圖片存在
修復前先確認圖片文件存在：
```bash
ls -la static/images/posts/POST_NAME/
```

#### 標題分隔線替換
```
Title
----
→ ## Title
```

**Hugo 自動轉換**：Hugo 會自動將 `----` 轉換為 h2 標題，主要檢查圖片語法即可

#### 代碼區塊修復
代碼部分需使用 ``` 包裹：
```
    code here    → ``` bash
    code here    → ```
```

#### HTML 轉 Markdown
Hugo 統一使用 Markdown 格式：

```
<h1>-<h6> → # - ######  
<pre><code>...</code></pre> → ``` language ... ```
<a href="url">text</a> → [text](url)
<strong>text</strong> → **text**
<em>text</em> → *text*
<ul><li>...</li></ul> → - ...
<ol><li>...</li></ol> → 1. ...
```

### Step 3: 驗證

```bash
# 建構驗證
hugo

# 圖片 HTML 輸出檢查
grep -o '<img[^>]*' public/posts/SLUG/index.html

# 標題 HTML 輸出檢查
grep -E '<h[1-6]' public/posts/SLUG/index.html

# 代碼區塊檢查
grep -E '<pre|<code' public/posts/SLUG/index.html
```

### Step 4: 本地預覽

```bash
# 啟動服務
hugo server -D

# 檢查服務狀態
curl -s -o /dev/null -w "%{http_code}" http://localhost:1313/
```

## 輸出格式

修復後產出清單：

| # | 文章 | 文章網址 | 修改項 | 數量 | 圖片存在 | 驗證 |
|---|------|----------|--------|------|----------|------|
| 1 | xxx | /posts/xxx/ | 圖片語法 | 8 | ✅ | ✅ |
| 2 | xxx | /posts/xxx/ | 標題分隔線 | 1 | - | ✅ |

## 驗證清單

根據問題類型進行驗證：

### 圖片連結問題
- [ ] 圖片文件存在 (`ls static/images/posts/NAME/`)
- [ ] 圖片語法正確 (`![alt](path)`)
- [ ] HTML 圖片輸出正確 (`<img`)

### HTML 格式問題
- [ ] HTML 標籤已轉為 Markdown (`<h1>` → `#`, `<pre>` → ```)
- [ ] HTML 輸出正確 (`<h1>-<h6>`, `<pre><code>`)

### 格式問題
- [ ] 標題分隔線已處理
- [ ] 代碼區塊已用 ``` 包裹

### 建構驗證
- [ ] Hugo 建構成功 (`hugo`)