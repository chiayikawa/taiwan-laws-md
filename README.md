# taiwan-laws-md　台灣全國法規 Markdown 版

隨著 AI 工具普及，Markdown 格式已成為語言模型最易讀取的文件格式。本專案將[全國法規資料庫](https://law.moj.gov.tw/)的所有中文法規轉換為 Markdown 檔案，供法律從業者、研究者及 AI 應用直接取用。所有內容以全國法規資料庫為唯一權威來源，每週自動同步更新。

## 使用方式

### 直接下載（方案 A）

Clone 整個 repo，之後 `git pull` 即可取得最新版本：

```bash
git clone https://github.com/YOUR_USERNAME/taiwan-laws-md.git
```

所有法規在 [`laws/`](laws/) 資料夾，共 1,343 部，一部一個 `.md` 檔。

### 自己跑（方案 B）

僅需 Python 與一個套件：

```bash
pip install httpx
python scripts/fetch_and_convert.py
```

執行後 `laws/` 底下即產生所有 Markdown 檔案。

## 更新頻率

每週一 10:00（台北時間）由 GitHub Actions 自動從全國法規資料庫 Open API 抓取最新資料並更新。

## 資料來源

[全國法規資料庫 Open API](https://law.moj.gov.tw/api/)，司法院及行政院授權開放資料。
