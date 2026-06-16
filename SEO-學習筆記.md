# SEO 學習筆記

> 以技術部落格情境整理的 SEO 知識點。每個主題依「**是什麼 → 為何影響排名 → 最佳實務**」說明,文末附 Hugo 實作範例供參考。

---

## 一、搜尋引擎如何運作(心智模型)

SEO 的一切都圍繞三個階段:

1. **Crawl(爬取)**:爬蟲沿著連結發現頁面 → 內部連結、sitemap、robots.txt 決定「能不能被找到」。
2. **Index(索引)**:解析 HTML、判斷主題與語言、儲存 → title/description/結構化資料/語言標示決定「如何被理解」。
3. **Rank(排名)**:依相關性、權威性、使用體驗排序 → 內容品質、連結、Core Web Vitals 決定「排多前」。

> 記憶法:**先讓它找得到 → 再讓它看得懂 → 最後讓它願意排前面。**

---

## 二、On-page SEO(頁面層)

### 1. Title 標籤
- **是什麼**:`<title>`,搜尋結果的藍色標題、瀏覽器分頁名。
- **為何重要**:權重最高的單一 on-page 因素之一;直接影響點擊率(CTR)。
- **最佳實務**:
  - 每頁唯一、描述精準、把重要關鍵字放前面。
  - 長度約 50–60 字元(英文)/約 30 字(中文),過長 SERP 會截斷。
  - 常見格式:`頁面標題 | 網站名`。

### 2. Meta description
- **是什麼**:`<meta name="description">`,搜尋結果標題下的摘要。
- **為何重要**:**不是排名因素,但強烈影響 CTR**;留白或與標題重複等於浪費。
- **最佳實務**:
  - 每頁獨特、120–160 字元、含關鍵字、像「廣告文案」吸引點擊。
  - 沒有自訂時,至少用文章首段(而非標題)當摘要。
  - 產生摘要要清掉雜訊:程式碼、圖片語法、HTML、控制字元(會破壞解析)。

### 3. 標題階層 H1–H6
- 每頁一個 `<h1>`(通常等於文章標題);H2/H3 形成內容大綱,幫助搜尋引擎理解結構,也利於精選摘要(featured snippet)。

### 4. 語言標示(lang / hreflang)
- **是什麼**:`<html lang>`、`og:locale`、多語站的 `hreflang`。
- **為何重要**:幫搜尋引擎判定內容語言、配對正確語系的使用者;標錯(內容中文卻標 `en`)會傷語言定位與無障礙。
- **最佳實務**:`lang` 要對應實際內容語言(如 `zh-TW`);多語版本互相宣告 `hreflang`。

---

## 三、結構化資料(Structured Data / Schema.org)

- **是什麼**:用 JSON-LD 以 schema.org 詞彙描述頁面語意(這是文章?作者是誰?麵包屑?),嵌在 `<script type="application/ld+json">`。
- **為何重要**:讓搜尋引擎更精準理解內容,並可觸發**複合式搜尋結果(rich results)**——作者、日期、麵包屑、評分等,提升能見度與 CTR。
- **常見類型**:
  - `WebSite` / `Organization` / `Person`:網站與發布者身分。**個人部落格用 `Person`,公司/品牌用 `Organization`**。
  - `BreadcrumbList`:麵包屑,SERP 顯示路徑。
  - `Article` / `BlogPosting`:文章的標題、作者、發布/修改時間、圖片、字數。
- **關鍵欄位**:`headline`、`author`、`datePublished`/`dateModified`、`image`、`publisher`、`mainEntityOfPage`。
- `sameAs`(指向作者/品牌的其他平台 URL)有助建立**知識圖譜**的實體關聯。
- ✅ 用 [Google Rich Results Test] / Schema Markup Validator 驗證。

---

## 四、社群分享中繼資料(Open Graph / Twitter Cards)

- **是什麼**:`og:*`(Facebook/LINE/Slack/LinkedIn 等通用)與 `twitter:*` 標籤,決定連結被分享時的**預覽卡片**。
- **為何重要**:雖非直接排名因素,但決定社群分享的點擊率與品牌呈現;缺圖的連結幾乎沒人點。
- **必備標籤**:
  - `og:title`、`og:description`、`og:type`(文章用 `article`)、`og:url`、`og:image`、`og:locale`、`og:site_name`。
  - `twitter:card`(有大圖用 `summary_large_image`)、`twitter:title`、`twitter:description`、`twitter:image`。
- **圖片規格**:建議 **1200×630**;務必設**全站預設分享圖**當沒有封面時的 fallback。

---

## 五、網站圖示(Favicon)

- **是什麼**:`favicon.ico` 及各尺寸 PNG、`apple-touch-icon`、`mask-icon` 等。
- **為何重要**:Google 行動版 SERP 會顯示 favicon;缺檔會造成**每頁多個 404**(浪費爬取預算、有損品質訊號)、品牌辨識度下降。
- **最佳實務**:備齊 `favicon.ico` + 16/32px PNG + 180px apple-touch-icon;確認模板引用的每個檔案都真的存在。

---

## 六、內容分類與內部連結

### 1. 標籤 / 分類(Taxonomies)
- 建立主題聚合頁,幫爬蟲發現相關內容、形成主題叢集(topic cluster);標籤也常用來填充結構化資料的 `keywords`。
- 標籤要**一致**(避免 `C#` 與 `csharp` 並存)、有意義、不過度氾濫。

### 2. 內部連結(Internal Linking)
- **為何重要**:傳遞頁面權重(link equity)、加深爬取、延長停留時間、降低跳出率。**是常被低估的高效益 SEO 槓桿**。
- **手法**:相關文章區塊、內文脈絡連結、麵包屑、主題叢集(支柱頁 ↔ 群集頁)。
- 相關性不足時「不連」優於「硬湊」——不相關連結稀釋權重也傷體驗。

---

## 七、URL 設計與「不斷鏈」

### 1. 乾淨 URL(Slug)
- 短、可讀、含關鍵字、用連字號分隔、小寫;避免特殊字元/空白/黏字。
- 技術名詞正規化以利可讀:`C#`→`csharp`、`C++`→`cpp`、`.NET`→`dotnet`。
- UTF-8 中文 URL 對 SEO 可接受(Google 能處理),但要注意百分比編碼帶來的可讀性。

### 2. Canonical(標準網址)
- `<link rel="canonical">` 告訴搜尋引擎「哪個是正本」,避免分頁、參數、別名造成的**重複內容**稀釋。

### 3. 改 URL 一定要轉址(301)
- **鐵則**:任何改變既有 URL 的動作,都要把舊網址 **301 轉址**到新網址,否則:
  - 既有外部連結與書籤失效(404)。
  - 已累積的搜尋排名/權重歸零。
- 靜態站常用 **alias / meta-refresh 轉址頁**達成等效效果。
- ⚠️ **重點坑**:轉址來源路徑要用**解碼後**的形式。伺服器收到請求會先 percent-decode 再找檔案;若以編碼路徑(`%E4%BD%BF…`)建立轉址,實際請求解碼後會 miss。

### 4. 圖片網址無法轉址
- HTML 頁能轉址,**圖片檔不能**。若圖片 URL 已被 Google 圖片索引,**直接刪除或改名 = 永久斷鏈、流量歸零**。換圖片格式/路徑前務必考慮這點。

---

## 八、Core Web Vitals 與效能

Google 的使用體驗排名訊號,三大指標:

| 指標 | 含義 | 主要對策 |
|---|---|---|
| **LCP**(Largest Contentful Paint) | 最大內容繪製時間(載入速度) | 圖片壓縮、`loading=lazy`、減少阻塞資源、CDN |
| **CLS**(Cumulative Layout Shift) | 版面位移(穩定度) | **圖片/影片設定 `width`/`height`**、為動態內容預留空間 |
| **INP**(Interaction to Next Paint) | 互動回應延遲 | 減少長任務、精簡 JS |

### 圖片是效能的最大施力點
1. **`alt` 文字**:無障礙 + 圖片搜尋的依據。應描述圖片內容;**檔名(`image1.png`)是無效 alt**。沒有更好資訊時,退而用文章標題勝過檔名。
2. **延遲載入**:離螢幕圖片加 `loading="lazy"`;搭配 `decoding="async"` 減少主執行緒阻塞。
3. **明確尺寸(防 CLS)**:`<img width height>` 讓瀏覽器載入前先預留正確比例的空間。
   - 搭配 CSS `img { max-width:100%; height:auto }` → 既防位移又能響應式縮放不變形。
4. **無失真壓縮**(像素不變、純去冗餘):
   - PNG:`optipng` / `oxipng` / `zopflipng`
   - JPEG:`jpegtran -optimize`(或 mozjpeg)
   - GIF:`gifsicle -O3`
   - 典型可省 20–30%。
5. **現代格式(WebP/AVIF)**:比 PNG/JPEG 更小(WebP 無失真常再省 ~30%)。但取捨要清楚:
   - 不支援的舊瀏覽器需 `<picture>` + 原圖 fallback → 等於**保留兩份**。
   - 結合「圖片不能轉址」:若已索引的原圖不能刪,WebP 只能用加法 → 評估**省下的頻寬 vs 多出的儲存/維護**是否划算。
   - 心法:**「技術可行」不等於「值得做」**,要看淨效益。

---

## 九、索引控制:robots.txt 與 Sitemap

- **robots.txt**:控制爬蟲可/不可爬的路徑,並指向 sitemap 位置。注意:`Disallow` 是「不要爬」,不等於「不要索引」(要 noindex 用 meta robots)。
- **XML Sitemap**:列出所有可索引 URL 與 `lastmod`,幫爬蟲有效率地發現/更新內容,大型站尤其重要。
- **meta robots** / `X-Robots-Tag`:`noindex` 才是真正阻止頁面進入索引(草稿、感謝頁等)。

---

## 十、SEO 工作的方法論

1. **優先序**:能被建置部署 → 內容層(title/description/語言/tags)→ 結構化資料與社群分享 → URL 健康度(乾淨 slug + 不斷鏈轉址)→ 內部連結 → Core Web Vitals。
2. **每個改動都要可驗證**:用真實輸出(產出的 HTML、sitemap)和具體數字佐證,而非「應該有效」。
3. **避免破壞性副作用**:改 URL 必附轉址;刪圖前確認索引狀態;批次改檔保留原格式、先 dry-run。
4. **驗證工具陷阱**:某些 locale 下 `grep` 用位元組比對範圍,會把 en-dash、彎引號的 UTF-8 位元組誤判成中文 → 用真正的 Unicode 比對(如 Python)才準。
5. **權衡而非堆功能**:每項優化都問「淨效益是否為正」,別為了「做點什麼」而引入維護債或風險。

---

## 附錄:Hugo 實作對照(範例)

| SEO 知識點 | Hugo 實作方式 |
|---|---|
| title / description / 語言 | `config` 的 `title`、`params.description`、`languageCode`;主題 `head` 模板 |
| 結構化資料 | 主題內建 schema 模板;`[params.schema] publisherType / sameAs` |
| OG / Twitter | 主題 `opengraph`/`twitter_cards` 模板;`params.images` 設預設分享圖 |
| tags | front matter `tags`;`/tags/` taxonomy 頁自動生成 |
| 乾淨 slug + 轉址 | front matter `slug` + `aliases`(產生 meta-refresh 轉址頁) |
| 相關文章 | `[related]` 設定 + `site.RegularPages.Related` |
| 圖片 alt/尺寸/lazy | **Render hook**(`layouts/_default/_markup/render-image.html`)統一輸出;尺寸可用 `data/*.json` 預存供查表 |
| sitemap / robots | `enableRobotsTXT`;Hugo 自動產生 sitemap |
| 本機驗證 | `hugo --gc --minify --cleanDestinationDir`、`hugo list all` |

> Hugo 的三大利器:**Render hooks**(不改內文統一調整輸出)、**Data files → `site.Data`**(預存建置期算不出的資料)、**模板覆寫**(與主題同名檔覆蓋行為)。
