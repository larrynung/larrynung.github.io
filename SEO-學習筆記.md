# Hugo 部落格 SEO 優化 — 學習筆記

> 以一個 Hugo + PaperMod、1600+ 篇文章的部落格為例,記錄本輪實作涵蓋的 SEO 知識點、技巧與決策思路。

---

## 0. 前置:先搞懂專案架構再動手

- **部署來源分支**:GitHub Pages 的 build workflow 設定 `on.push.branches`,本站部署來源是 `hugo` 分支(非 `master`)。動手前先確認「哪個分支才是真正會被建置部署的原始碼」。
- **主題是 git submodule**:`themes/PaperMod` 透過 `.gitmodules` 引入,需 `git submodule update --init` 才能取得;主題版本由記錄的 commit SHA 決定。
- **Hugo 版本相容性**:主題會宣告最低 Hugo 版本(PaperMod 需 `≥0.146`)。workflow 釘的版本若低於它會建置失敗 → 部署前務必本機用相同版本驗證。
- **本機驗證建置**:
  ```bash
  hugo --gc --minify                 # 一般建置
  hugo --gc --minify --cleanDestinationDir  # 清掉殘留,避免舊檔污染驗證
  hugo list all                      # 匯出所有頁面的 path/slug/permalink (CSV)
  ```
  ⚠️ 多次建置不清 `public/` 會殘留舊檔,讓你誤判結果。驗證 URL/別名時一定要 `--cleanDestinationDir`。

---

## 1. On-page 基礎:title / description / 語言

### Meta description
- **問題模式**:description 直接複製 title、或留空 → 搜尋摘要(snippet)毫無資訊量。
- **PaperMod 的 fallback 順序**:`.Description` → `.Summary` → `site.Params.description`。
- **做法**:從正文首段自動產生 ~120–150 字描述,於句子邊界(。！？)截斷。清理時要移除:程式碼區塊、圖片語法、HTML 標籤、shortcode、Markdown 連結/行內碼、清單/標題符號、**控制字元**(如 `\x08`,常來自貼上的 Windows 路徑,會讓 YAML 解析失敗)。
- description 會同時餵給 `<meta name=description>`、`og:description`、`twitter:description`、JSON-LD。

### 語言標示
- 內容是繁中卻設 `languageCode='en'` → `<html lang=en>`、`og:locale=en`,不利搜尋引擎語言判定。
- 修正:
  ```toml
  defaultContentLanguage = 'zh-tw'
  languageCode = 'zh-TW'
  hasCJKLanguage = true   # CJK 字數統計/摘要正確
  ```

---

## 2. 結構化資料(JSON-LD / schema.org)

- PaperMod 內建三種:首頁 `WebSite`/`Person`/`Organization`、列表頁 `BreadcrumbList`、文章頁 `BlogPosting`。
- **個人部落格要設 `publisherType = "Person"`**(預設是 Organization):
  ```toml
  [schema]
  publisherType = "Person"
  sameAs = ["https://github.com/larrynung"]   # 建立作者跨平台實體關聯(知識圖譜)
  ```
- `BlogPosting` 的 `keywords` 由 `tags` 填充 → tags 缺失會讓結構化資料不完整。

---

## 3. 社群分享:Open Graph / Twitter Cards

- **預設分享圖**:多數文章無 cover → 分享無預覽圖。PaperMod 的 `get-page-images` 有 site-level fallback:
  ```toml
  images = ["images/og-default.png"]   # 規格 1200×630
  ```
- 順序:文章 `cover.image` > 頁面圖片資源 > `site.Params.images`。
- Twitter card 有圖時自動升級 `summary_large_image`。

---

## 4. Favicon(別忽略 404)

- 主題 `head.html` 會引用一整組 icon(`favicon.ico`、`favicon-16x16.png`、`favicon-32x32.png`、`apple-touch-icon.png`、`safari-pinned-tab.svg`),**檔案不存在就是每頁 5 個 404**。
- 用 PIL 從一張來源圖產生各尺寸:
  ```python
  from PIL import Image
  im = Image.open('favicon.ico').convert('RGBA')
  im.resize((180,180), Image.LANCZOS).save('apple-touch-icon.png')
  ```

---

## 5. 標籤 / Taxonomies

- 缺 tags 的影響:標籤頁無法發現相關文章、JSON-LD keywords 為空、相關文章功能失效。
- **批次補 tags 策略**:用既有 tag 詞彙表 + 標題關鍵字規則(regex)自動對應;少數無法匹配的手動補。只對「無 tags」的文章操作,不覆蓋既有。

---

## 6. URL / slug 與「不斷鏈」的鐵則

- **slug 品質**:含 `[ ]`、空白、技術符號的 slug,Hugo urlize 後會變黏字(`csharpvb.netpath...`)。重產乾淨 slug:標點轉連字號、保留 CJK、技術名詞正規化(`C#`→`csharp`、`C++`→`cpp`、`VB.NET`→`vbnet`、`.NET`→`dotnet`)。
- **改 URL 必加 `aliases`(301/meta-refresh 轉址)**,否則既有外部連結與 Google 索引會斷:
  ```yaml
  slug: "csharp-vbnet-numeric-operations-with-nothing-or-null"
  aliases: ["/posts/csharpvb.net使用nothing或null作數值運算/"]
  ```
- 🔑 **關鍵坑**:alias 要用**解碼後**的路徑。GitHub Pages 收到請求會先 percent-decode 再找檔案;若 alias 寫成 `%E4%BD%BF...` 編碼路徑,Hugo 會在字面編碼路徑建檔,實際請求解碼後就 miss。用 `hugo list all` 拿到的 permalink 是編碼的,要 `urllib.parse.unquote` 後再寫入。
- **改 URL 前先從「原始上線狀態」擷取現行網址當 alias 基準**——若中途已有未部署的中間分支,別拿中間網址當基準,要拿真正被索引的線上網址。

---

## 7. 內部連結:相關文章

- 內部連結提升爬取深度與權重傳遞,也增加停留時間。
- Hugo 內建 Related Content API:
  ```toml
  [related]
    includeNewer = true
    threshold = 80
    [[related.indices]]
      name = "tags"
      weight = 100
    [[related.indices]]
      name = "date"
      weight = 10
  ```
- PaperMod 無相關文章擴充點 → 覆寫 `layouts/_default/single.html`,在 footer 用:
  ```go-html-template
  {{ $related := site.RegularPages.Related . | first 5 }}
  {{ with $related }} ... {{ end }}
  ```
- 相關度不足者「不顯示」優於「硬湊不相關連結」。

---

## 8. 圖片 SEO 與效能(Core Web Vitals)

### alt 文字
- 約 7000 張 alt 是檔名(`image_thumb.png`)→ 對圖片索引/無障礙無價值。
- **不動內文的做法**:覆寫 render hook,偵測「空/`image`/檔名格式」的 alt 時自動改用**文章標題**:
  ```go-html-template
  {{ $isFilename := or (not (trim .Text " "))
       (findRE `(?i)^[\w\-. ]+\.(png|jpe?g|gif|webp)$` (trim .Text " ")) }}
  {{ if $isFilename }}{{ $alt = .Page.Title }}{{ end }}
  ```

### 載入效能
- `loading="lazy"`(離螢幕延遲載入,PaperMod 已內建)+ `decoding="async"`。

### CLS(版面位移)
- 圖片缺 `width`/`height` → 載入前無法預留空間 → CLS 升高(Core Web Vitals 排名因素)。
- static 圖片非 Hugo resource,拿不到尺寸 → **用 PIL 預算尺寸寫成 `data/imgdims.json`**,render hook 查表補上:
  ```go-html-template
  {{ with index (.Page.Site.Data.imgdims | default dict) $u.Path }}
    {{ $width = string (index . 0) }}{{ $height = string (index . 1) }}
  {{ end }}
  ```
- ⚠️ 補尺寸屬性前,CSS 必須有 `img { height: auto }`(PaperMod reset 只有 `max-width:100%`),否則窄螢幕會壓扁變形。

### 無失真壓縮
- 工具(皆 lossless):
  ```bash
  optipng -o2 -strip all <png>           # PNG
  jpegtran -optimize -copy none ...       # JPEG
  gifsicle -O3 <gif>                       # GIF
  ```
- 成效:375MB → 285MB(−24.8%),像素與尺寸不變,不影響 width/height。

### WebP 的取捨(為什麼最後沒做)
- WebP 無失真比優化後 PNG 再省 ~31%,但要安全上線需 `<picture>` + 保留原圖 fallback。
- **不做的理由**:
  1. 約 3-4% 舊瀏覽器不支援 → 沒原圖會破圖;
  2. **圖片無法做 301 轉址**,既有被索引的 `.png` 網址直接刪會斷鏈丟圖片流量。
- 結論:若必須保留原圖(repo 多一份重複檔),效益/成本不划算 → 放棄。**「能做」不等於「該做」**。

---

## 9. Hugo 實用技巧彙整

| 技巧 | 用途 |
|---|---|
| **Render hooks** (`layouts/_default/_markup/render-image.html`) | 不改內文,統一調整所有 Markdown 圖片/連結的輸出 |
| **Data files** (`data/*.json` → `site.Data`) | 把建置期算不出的資訊(圖片尺寸)預先備好供模板查表 |
| **Partial / layout override** | 與主題同名檔覆蓋主題行為;`extend_head.html`/`extend_footer.html` 是無侵入式插入點 |
| **`hugo list all`** | 匯出 path↔permalink 對照,做 URL 遷移/別名的基準 |
| **`site.RegularPages.Related`** | 內建相關內容 |
| `[related]` / `[schema]` / `images` / `aliases` | 設定即生效的 SEO 開關 |

---

## 10. 流程與工程紀律

- **每個改動獨立成 PR**,標題/說明寫清楚「問題 → 做法 → 驗證數據」。
- **改動前後都用真實建置驗證**,並用具體數字佐證(頁數、別名數、檔案大小、剩餘缺口數)。
- **批次改 1600+ 檔的安全網**:解析 front matter 時保留原格式(YAML `---` / TOML `+++` 各自語法);逐筆驗證(如翻譯前後比對原標題吻合)再寫入;先 dry-run 統計再實寫。
- **驗證工具的陷阱**:`grep [一-鿿]` 在某些 locale 會用位元組比對,把 en-dash、彎引號的 UTF-8 位元組誤判為 CJK → 用 Python 的 unicode 比對才準。
- **覆寫主題檔的代價**:會有主題升級時的維護成本;submodule 釘版可降低風險,但要記得這些是「自訂層」。
- **大型背景任務**:壓縮/轉檔放背景跑,完成前不要提交;用 `until ! pgrep ...; do sleep; done` 等待。

---

## 一句話總結

> SEO 優化的順序大致是:**先讓站台能正確建置部署** → **內容層(title/description/語言/tags)** → **結構化資料與社群分享** → **URL 健康度(乾淨 slug + 不斷鏈的 aliases)** → **內部連結** → **Core Web Vitals(alt/lazy/CLS/體積)**。每一步都要本機建置驗證,且任何會改變既有 URL 的動作都必須附帶轉址。
