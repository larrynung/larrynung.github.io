+++
title = "Coze Studio - Getting Started"
date = "2025-08-11T00:05:59+08:00"
tags = ["Coze Studio", "AI", "開源", "Docker"]
draft = false
+++

Coze Studio 是一個開源的AI應用開發平台，本文將介紹如何在本地環境中部署與使用。

## 環境需求

在開始之前，請確保系統符合以下要求：

- CPU: 2 核心以上
- 記憶體: 4 GB 以上（建議8GB以上）
- 已安裝並運行 Docker 和 Docker Compose

## 部署步驟

### 1. 取得原始碼

首先，我們需要克隆 Coze Studio 的代碼倉庫：

```bash
git clone https://github.com/coze-dev/coze-studio.git
cd coze-studio
```

![克隆代碼庫](/images/coze-studio/git-clone.png)

### 2. 配置模型

Coze Studio 需要配置模型才能正常運作，我們需要複製並修改模型配置：

```bash
cp backend/conf/model/template/model_template_ark_doubao-seed-1.6.yaml \
   backend/conf/model/ark_doubao-seed-1.6.yaml
```

### 3. 修改配置文件

接下來，我們需要編輯模型配置文件：

1. 進入配置目錄：`backend/conf/model`
2. 編輯 `ark_doubao-seed-1.6.yaml` 文件
3. 設置以下必要參數：
   - `id`: 設置一個唯一的數字ID
   - `meta.conn_config.api_key`: 填入 Volcengine Ark API Key
   - `meta.conn_config.model`: 設定模型端點

![模型配置](/images/coze-studio/model-config.png)

### 4. 啟動服務

完成配置後，我們可以啟動 Coze Studio 服務：

```bash
cd docker
cp .env.example .env
docker compose up -d
```

> 注意：首次啟動時，Docker 會下載所需的鏡像，這可能需要一些時間。

![啟動服務](/images/coze-studio/run-service.png)

### 5. 訪問 Coze Studio

服務啟動完成後，在瀏覽器中訪問：

```
http://localhost:8888/
```

![Coze Studio 首頁](/images/coze-studio/service-started.png)
