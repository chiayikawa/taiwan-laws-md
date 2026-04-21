# 台灣全國法規資料庫 Markdown 版 taiwan-laws-md　

隨著 AI 工具普及，Markdown 格式已成為語言模型最易讀取的文件格式。本專案將[全國法規資料庫](https://law.moj.gov.tw/)的所有中文法規轉換為 Markdown 檔案，供法律從業者、研究者及 AI 應用直接取用。所有內容以全國法規資料庫為唯一權威來源，每週自動同步更新。

## 使用方式

```bash
git clone https://github.com/chiayikawa/taiwan-laws-md.git
```

下載後直接在 [`laws/`](laws/) 資料夾查找所需法規，共 1,343 部，一部一個 `.md` 檔。之後執行 `git pull` 即可取得最新版本。

## 更新頻率

每週一 10:00（台北時間）自動從全國法規資料庫 Open API 抓取最新資料並更新。

## 資料來源

[全國法規資料庫 Open API](https://law.moj.gov.tw/api/)，司法院及行政院授權開放資料。
