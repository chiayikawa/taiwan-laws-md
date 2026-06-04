# taiwan-laws-md

[![Update Taiwan Laws](https://github.com/chiayikawa/taiwan-laws-md/actions/workflows/update.yml/badge.svg)](https://github.com/chiayikawa/taiwan-laws-md/actions/workflows/update.yml)
[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Data License: OGL Taiwan 1.0](https://img.shields.io/badge/data-OGL%20Taiwan%201.0-green.svg)](DATA_LICENSE.md)

台灣全國法規資料庫 Markdown 版。

本專案將[全國法規資料庫](https://law.moj.gov.tw/)的中文法規轉換為一部法律一個 Markdown 檔，供法律研究、開放資料、搜尋索引、Obsidian 知識庫、RAG 與 AI 法律工具直接取用。所有法規內容以全國法規資料庫為權威來源，並由 GitHub Actions 每週自動同步更新。

## 專案價值

台灣法規資料雖然已公開，但原始資料格式不適合直接放進一般開發者、研究者與 AI workflow。本專案把法規整理成可版本控管、可搜尋、可引用、可直接餵給語言模型的 Markdown corpus，降低 civic tech、法律科技、研究與教育專案使用台灣法律資料的門檻。

目前資料集包含 1,345 部法規，位於 [`laws/`](laws/)，並提供 [`index.json`](index.json) 作為機器可讀 metadata 索引。

## 使用方式

```bash
git clone https://github.com/chiayikawa/taiwan-laws-md.git
cd taiwan-laws-md
```

下載後可直接在 [`laws/`](laws/) 資料夾查找法規。之後執行 `git pull` 即可取得最新版本。

```bash
ls laws
sed -n '1,80p' laws/中華民國刑法.md
```

## 適合用途

- 建立台灣法規全文搜尋或索引。
- 建立法律 RAG、AI 法律助理或法律研究工具。
- 將法規放入 Obsidian、Logseq、Markdown wiki 或內部知識庫。
- 追蹤每週法規修正，並以 Git diff 檢查變更。
- 為開放資料、公民科技、法律教育與研究專案提供可讀資料基礎。

## 更新頻率

每週一 10:00（台北時間）自動從全國法規資料庫 Open API 抓取最新資料並更新。也可以在 GitHub Actions 手動執行更新 workflow。

更新流程：

1. 從全國法規資料庫 Open API 下載最新法規 JSON。
2. 將每部法規轉換為獨立 Markdown 檔。
3. 產生 `index.json` metadata。
4. 驗證輸出資料集。
5. 若資料有變更，自動提交到 `main`。

## 本機維護

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/fetch_and_convert.py
python3 scripts/validate_dataset.py
```

## 資料格式

每個 Markdown 檔包含：

- 法規名稱
- 法規類別
- 修正日期
- 生效或廢止說明
- 原始法規網址
- 條文內容

範例：

```text
法規名稱：中華民國刑法
法規類別：...
修正日期：...
法規網址：https://law.moj.gov.tw/...

第 1 條
...
```

`index.json` 包含每部法規的名稱、類別、位階、修正日期、官方網址與 Markdown 檔案路徑，適合用於搜尋索引、資料管線與 RAG 前處理。

## 路線圖

- 產生機器可讀的 `index.json` metadata。
- 提供依法規名稱、類別、修正日期查詢的 CLI。
- 產生每週法規變更摘要。
- 建立 RAG-friendly chunked export。
- 提供 MCP server 或 API wrapper，讓 AI agent 可直接查詢台灣法規。

## 貢獻

歡迎回報格式錯誤、資料缺漏、法規更新問題，以及提出工具整合需求。請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 授權

本專案程式碼採用 [MIT License](LICENSE)。

法規資料來源為全國法規資料庫 Open API，資料使用規範與來源標示請見 [DATA_LICENSE.md](DATA_LICENSE.md)。本專案不是政府官方網站，也不提供法律意見；實際引用或法律行動請以全國法規資料庫公告內容為準。

## 資料來源

- [全國法規資料庫](https://law.moj.gov.tw/)
- [全國法規資料庫 Open API](https://law.moj.gov.tw/api/)
