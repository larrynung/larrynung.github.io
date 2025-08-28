---
description: 建立與發布 Hugo 部落格文章的工作流程指南
auto_execution_mode: 1
---

# Hugo 文章新增與發布工作流程

## 1. 建立新文章

### 1.1 使用 Hugo 指令建立文章

```bash
# 切換到專案根目錄
cd /path/to/your/hugo/site

# 建立新文章（會自動建立目錄和 index.md）
hugo new content content/posts/文章名稱/index.md
```

**思考過程**：
- 使用 `hugo new` 指令可以確保 front matter 格式正確
- 將每篇文章放在獨立目錄中，方便管理相關資源
- 使用英文命名目錄，避免路徑問題

### 1.2 編輯 front matter

```yaml
+++
title = '文章標題（建議使用繁體中文）'
date = 2025-08-14T00:00:00+08:00  # 使用實際日期
draft = true  # 完成後改為 false 發布
tags = ['標籤1', '標籤2']  # 使用簡潔的標籤
+++
```

**注意事項**：
- 日期格式必須符合 ISO 8601 標準
- 使用有意義的標籤，方便後續分類與搜尋
- 保持 draft 為 true，直到文章完成並準備發布

## 2. 圖片管理

### 2.1 圖片存放位置

```
static/
  images/
    posts/
      文章名稱/          # 使用與文章目錄相同的名稱
        image1.png
        image2.jpg
```

**思考過程**：
- 將圖片放在 `static/images/posts/文章名稱/` 目錄下
- 使用描述性的檔案名稱
- 保持圖片檔案名稱全小寫，使用連字符分隔單詞

### 2.2 在文章中插入圖片

```markdown
{% img /images/posts/文章名稱/image1.png %}
```

或使用 Markdown 語法：

```markdown
![圖片說明](/images/posts/文章名稱/image1.png)
```

**最佳實踐**：
- 使用 Hugo 的 `img` shortcode 可以更好地控制圖片顯示
- 為每張圖片提供有意義的替代文字
- 保持圖片大小適中，建議寬度不超過 1200px

## 3. 文章內容撰寫

### 3.1 標題層級

```markdown
# 主標題（H1）

## 章節標題（H2）

### 小節標題（H3）
```

**注意**：
- 避免跳過標題層級（例如：H1 後直接接 H3）
- 保持標題簡潔明瞭

### 3.2 程式碼區塊

````markdown
```javascript
// 使用三個反引號指定語言
function example() {
  console.log('Hello, World!');
}
```
````

## 4. 預覽與發布

### 4.1 本地預覽

```bash
# 啟動本地開發伺服器
hugo server -D
```

**檢查清單**：
- [ ] 所有圖片是否正確顯示
- [ ] 標題層級是否正確
- [ ] 程式碼區塊是否正確標記語言
- [ ] 所有連結是否有效

### 4.2 發布文章

1. 將 `draft` 改為 `false`
2. 提交變更到 Git
3. 推送到遠端儲存庫

## 5. 回饋與改進

- 定期檢查網站的 Google Analytics 數據
- 收集讀者回饋
- 根據數據和回饋持續優化內容

## 常見問題

### Q: 如何更新現有文章？
A: 直接編輯對應的 markdown 文件，保持相同的檔案路徑和 front matter 格式。

### Q: 如何處理多張相關圖片？
A: 建立子目錄來組織相關圖片，例如：
```
static/images/posts/文章名稱/diagrams/
static/images/posts/文章名稱/screenshots/
```

### Q: 如何確保圖片在行動裝置上顯示正常？
A: 使用響應式圖片語法，並確保圖片大小適中。

---
*最後更新：2025 年 8 月 14 日*