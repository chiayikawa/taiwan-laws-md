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
INDEX_PATH = Path(__file__).parent.parent / "index.json"


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


def law_filename(law_name: str) -> str:
    safe_name = law_name.replace("/", "／").replace("\\", "＼")
    return f"{safe_name}.md"


def build_index(laws: list[dict]) -> list[dict]:
    index = []
    for law in laws:
        index.append(
            {
                "name": law["LawName"],
                "category": law.get("LawCategory"),
                "level": law.get("LawLevel"),
                "modified_date": law.get("LawModifiedDate"),
                "effective_note": law.get("LawEffectiveNote"),
                "abandon_note": law.get("LawAbandonNote"),
                "url": law.get("LawURL"),
                "file": f"laws/{law_filename(law['LawName'])}",
            }
        )
    return sorted(index, key=lambda item: item["name"])


def convert_all(laws: list[dict], out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    expected_paths = set()
    for law in laws:
        path = out_dir / law_filename(law["LawName"])
        expected_paths.add(path)
        path.write_text(law_to_md(law), encoding="utf-8")

    for stale_path in out_dir.glob("*.md"):
        if stale_path not in expected_paths:
            stale_path.unlink()

    print(f"  Written {len(laws)} files to {out_dir}/")


if __name__ == "__main__":
    laws = fetch_laws()
    convert_all(laws, OUT_DIR)
    INDEX_PATH.write_text(
        json.dumps(build_index(laws), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  Written metadata index to {INDEX_PATH}")
    print("Done.")
