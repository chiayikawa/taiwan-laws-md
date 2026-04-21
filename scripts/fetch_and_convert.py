#!/usr/bin/env python3
"""
Taiwan Laws → Markdown converter
Fetches all laws from 全國法規資料庫 Open API and converts to Markdown.
"""

import io
import json
import zipfile
from pathlib import Path

import httpx

API_URL = "https://law.moj.gov.tw/api/ch/law/json"
OUT_DIR = Path(__file__).parent.parent / "laws"


def fetch_laws() -> list[dict]:
    print("Fetching laws from API...")
    r = httpx.get(API_URL, timeout=60, follow_redirects=True)
    r.raise_for_status()
    zf = zipfile.ZipFile(io.BytesIO(r.content))
    json_file = next(n for n in zf.namelist() if n.endswith(".json"))
    data = json.loads(zf.read(json_file).decode("utf-8-sig"))
    laws = data["Laws"]
    print(f"  {len(laws)} laws fetched (updated {data['UpdateDate']})")
    return laws


def law_to_md(law: dict) -> str:
    lines = []

    lines.append(f"法規名稱：{law['LawName']}")
    lines.append(f"法規類別：{law['LawLevel']} / {law['LawCategory']}")
    if law.get("LawModifiedDate"):
        lines.append(f"修正日期：{law['LawModifiedDate']}")
    if law.get("LawEffectiveNote"):
        lines.append(f"生效狀態：{law['LawEffectiveNote']}")
    if law.get("LawAbandonNote"):
        lines.append(f"廢止說明：{law['LawAbandonNote']}")
    lines.append(f"法規網址：{law['LawURL']}")

    if law.get("LawForeword"):
        lines.append("")
        lines.append(law["LawForeword"].replace("\r\n", "\n"))

    for article in law.get("LawArticles", []):
        content = article["ArticleContent"].replace("\r\n", "\n").replace("\r", "\n")
        if article["ArticleType"] == "C":
            lines.append("")
            lines.append(content)
        else:
            lines.append("")
            lines.append(article["ArticleNo"])
            lines.append(content)

    return "\n".join(lines).strip() + "\n"


def convert_all(laws: list[dict], out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for law in laws:
        name = law["LawName"]
        safe_name = name.replace("/", "／").replace("\\", "＼")
        path = out_dir / f"{safe_name}.md"
        path.write_text(law_to_md(law), encoding="utf-8")
    print(f"  Written {len(laws)} files to {out_dir}/")


if __name__ == "__main__":
    laws = fetch_laws()
    convert_all(laws, OUT_DIR)
    print("Done.")
